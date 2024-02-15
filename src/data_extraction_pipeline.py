from src.fetchReview import GoogleAppReviewExtractionPipeline,AppleAppReviewExtractionPipeline
import os
import pandas as pd
from datetime import datetime

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
        print("Class objects create for review extraction")
        apple_reviews = AppleAppReviewExtractionPipeline(self.apple_app_id)
        apple_reviews_df = apple_reviews.extract_reviews()
        
        google_reviews = GoogleAppReviewExtractionPipeline(self.google_app_id)
        google_reviews_df = google_reviews.extract_reviews()
        return google_reviews_df, apple_reviews_df
    
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
        print("Data Standardization complete")
        
        return all_reviews_df
    def write(self):
        df = self.combine_reviews()
        if os.path.exists(self.output_path):
            final_path = os.path.join(self.output_path,str(datetime.today().date())+"_reviews.csv")
        else:
            os.makedirs(self.output_path)
            final_path = os.path.join(self.output_path,"_reviews.csv")
        df.to_csv(final_path,index=False)
        print(f"Successfully Written data into %s" % final_path)