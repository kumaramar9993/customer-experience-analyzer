import os
from src import fetchReview
from src.data_extraction_pipeline import ReviewExtractionPipeline

app_info = {
    "google_play_store_info":'com.phonepe.app',
    "apple_play_store_info" :"https://apps.apple.com/in/app/phonepe-secure-payments-app/id1170055821"
}
rep = ReviewExtractionPipeline(company_name="PhonePe",app_info=app_info)
rep.write()
