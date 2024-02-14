from google_play_scraper import Sort, reviews_all
from app_store_scraper import AppStore
import pandas as pd

class GoogleAppReviewExtractionPipeline():
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


class AppleAppReviewExtractionPipeline():
    def __init__(self,app_url):
        app_id = app_url.split("/")[-1].replace("id","")
        file_name = app_url.split("/")[-2].replace("-","_")
        self.app_id = app_id
        self.file_name = file_name
    def extract_reviews(self):
        reviews_list = AppStore(country="IN",app_name=self.file_name, app_id=self.app_id)
        reviews_list.review()
        return pd.DataFrame(reviews_list.reviews)
    
