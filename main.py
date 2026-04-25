
from Create_post import create_post
from Get_Post import Post_tweet
try:
    post=create_post()
    print(post)
    Post_tweet(post)
    print('Done')
except Exception as e:
    print(e.with_traceback())

