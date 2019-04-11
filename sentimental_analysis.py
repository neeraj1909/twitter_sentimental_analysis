import twitter

# initialize api instance
twitter_api = twitter.Api(consumer_key='ikFRNPqbwbvf9IksPHn5oeLnl',
                        consumer_secret='V2zCXEgYiF3jaNWrN4m75x1ZFcnmANZrJ5cwnIFLCtubruI853',
                        access_token_key='4864531754-xe6jxjmvPARuuwFT8uF2lI3PDDavnt1bRhc1BYb',
                        access_token_secret='N5n5Tgnt3SUHYsNw83GfeaS9N0IqfzaCTgNzysIjlhOr')

# test authentication
print(twitter_api.VerifyCredentials())