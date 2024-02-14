import pandas as pd
import os
# from fetchReview import GoogleAppReviewExtractionPipeline,AppleAppReviewExtractionPipeline

from google_play_scraper import Sort, reviews_all
from app_store_scraper import AppStore
import pandas as pd

class GoogleAppReviewExtractionPipeline:
    def __init__(self,app_id):
        self.app_id = app_id
    
    def extract_review(self):
        reviews_list = reviews_all(
            self.app_id,
            sleep_milliseconds=0, # defaults to 0
            lang='en', # defaults to 'en'
            country='in', # defaults to 'us'
            sort=Sort.NEWEST, # defaults to Sort.MOST_RELEVANT
            filter_score_with=None # defaults to None(means all score)
        )
        reviews_df = pd.DataFrame(reviews_list)
        return reviews_df


class AppleAppReviewExtractionPipeline:
    def __init__(self,app_url):
        app_id = app_url.split("/")[-1].replace("id","")
        file_name = app_url.split("/")[-2].replace("-","_")
        self.app_id = app_id
        self.file_name = file_name
    def extract_reviews(self):
        reviews_list = AppStore(country="IN",app_name=self.file_name, app_id=self.app_id)
        reviews_list.review()
        return pd.DataFrame(reviews_list.reviews)
    


class ReviewExtractionPipeline():
    def __init__(self,company_name,app_info):
        self.company_name = company_name
        self.google_app_id = app_info["google_play_store_info"]
        self.apple_app_id = app_info["apple_play_store_info"]
        
        # self.google_app_id = self.google_store_info.app_id
        # self.apple_app_id = self.apple_store_info.app_url
        dirname = os.path.dirname(__file__)
        self.output_path = os.path.join(dirname, "data",company_name)

    def extract_review(self):
        google_reviews = GoogleAppReviewExtractionPipeline(self.google_app_id)
        apple_reviews = AppleAppReviewExtractionPipeline(self.apple_app_id)
        return google_reviews, apple_reviews
    
    def combine_reviews(self):

        # extracting review
        google_df, apple_df = self.extract_review()
        
        # app review - rearranging columns
        apple_df["content"] = apple_df[["title","review"]].fillna("").agg('. '.join, axis=1)
        apple_df.loc[:,"thumbsUpCount"] = 1
        apple_df = apple_df[["date","rating","thumbsUpCount","content"]]
        apple_df.columns = ["date","rating","thumbsUpCount","review"]
        apple_df.loc[:,"source"] = "Apple Play Store"

        # google review - rearranging columns
        google_df = google_df[["at","score","thumbsUpCount","content"]]
        google_df.columns = ["date","rating","thumbsUpCount","review"]
        google_df.loc[:,"source"] = "Google Play Store"
        
        # combining reviews
        all_reviews_df =  pd.concat([google_df,apple_df],axis=0)
        
        return all_reviews_df
    def write(self):
        df = self.combine_reviews()
        df.to_csv(self.output_path,index=False)

        
        
if __name__ =='__main__':
    app_info = {
        "google_play_store_info":'com.phonepe.app',
        "apple_play_store_info" :"https://apps.apple.com/in/app/phonepe-secure-payments-app/id1170055821"
    }
    rep = ReviewExtractionPipeline(company_name="PhonePe",app_info=app_info)
    rep.write()


    
