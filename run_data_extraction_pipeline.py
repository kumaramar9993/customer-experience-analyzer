import os
from src import fetchReview
from src.data_extraction_pipeline import ReviewExtractionPipeline

# Ingest Phonepe Reviews
app_info = {
    "google_play_store_info":'com.phonepe.app',
    "apple_play_store_info" :"https://apps.apple.com/in/app/phonepe-secure-payments-app/id1170055821"
}
rep = ReviewExtractionPipeline(company_name="PhonePe",app_info=app_info)
rep.write()

# Ingest Google Pay Reviews
app_info1 = {
    "google_play_store_info":'com.google.android.apps.nbu.paisa.user',
    "apple_play_store_info" :"https://apps.apple.com/in/app/google-pay-save-pay-manage/id1193357041"
}
rep = ReviewExtractionPipeline(company_name="GooglePay",app_info=app_info)
rep.write()
