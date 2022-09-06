import tweepy
import time
 
API_KEY = "02os7L4AzZaKLVe62f1AYGXDP"
API_SECRET = "Bp45yQaftxTXvoCYUSpnbTlnluWDlpe50GyExliB3pM64Lo18l"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAKwegwEAAAAArAzbR%2BtrCqYawKy7voZ3%2FxghoEk%3DnFrhAm9pCXSVxB9Au5DlmOCstnKLKycIKte2InjiLcyZZCoeuC"
ACCESS_TOKEN = "1567078526913839110-Z0AgC518ezrb4sAMEwgCCKQNlVPYrR"
ACCESS_SECRET = "TWnysuhpvKWowaJpHSWydsOBEknmnRqCCA1KIrrs4Z1zO"
 
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
 
api = tweepy.API(auth)

def PublicarTweet(message):
    api.update_status(status=message)

PublicarTweet("Preferiría no hacerlo")