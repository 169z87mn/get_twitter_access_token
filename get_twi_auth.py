import tweepy

# keys
consumer_token = 'consumer_token'
consumer_secret = 'consumer_secret'

auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
redirect_url = auth.get_authorization_url()

print(f'Login to: {redirect_url}')

verifier = input('PIN: ').strip()
auth.get_access_token(verifier)

print(f'access_token: {auth.access_token}')
print(f'access_token_secret: {auth.access_token_secret}')
