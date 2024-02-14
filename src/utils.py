def get_reviews(bank_app_id):
    reviews = reviews_all(bank_app_id,
                    sleep_milliseconds=0, # defaults to 0
                    lang='en', # defaults to 'en'
                    country='uk', # defaults to 'us'
                    sort=Sort.NEWEST, # defaults to Sort.MOST_RELEVANT
                    filter_score_with=None # defaults to None(means all score)
            )
    return reviews

