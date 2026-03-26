from Fetch_Data import create_post
from Get_Post import Post_tweet

try:
    post=create_post()
    Post_tweet(post)
    print('Done')
except Exception as e:
    pass

