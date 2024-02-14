import pandas as pd
import os
from fetchReview import GoogleAppReviewExtractionPipeline,AppleAppReviewExtractionPipeline

class ReviewExtractionPipeline():
    def __init__(self,company_name,app_info,output_file):
        self.company_name = company_name
        self.output_file = output_file
        self.google_store_info = app_info["google_play_store_info"]
        self.apple_store_info = app_info["apple_play_store_info"]
        
        self.google_app_id = self.google_store_info.app_id
        self.apple_app_id = self.apple_store_info.app_url

        self.filename = os.path.basename(output_file)
        self.images_dir = f"images/input/{os.path.basename(self.pdffile)[:-4]}/"
        
        
    def extract_review(self):
        google_reviews = GoogleAppReviewExtractionPipeline(self.google_app_id)
        apple_reviews = AppleAppReviewExtractionPipeline(self.app_url)
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
        df.to_csv()
        
        


    
