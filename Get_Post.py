import tweepy

import os




def Post_tweet(text):
    try:
        client = tweepy.Client(
        consumer_key=os.getenv('X_api_key'),
        consumer_secret=os.getenv('X_api_secrete'),
        access_token=os.getenv('X_AccessToken'),
        access_token_secret=os.getenv('X_Access_Token_Secret')
        )

        
        client.create_tweet(text=text)
    except Exception as e:
        print(e)
