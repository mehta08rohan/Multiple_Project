import tweepy
from textblob import TextBlob

consumer_key ='EctrBfByU8R8i6gL1MVcdSDcg'
consumer_key_secret = 'Dc2L6aTkj3TX3VMpU2aoY9zAEwRbuO5A4xCnwKdoH1I3XhA0eZ'

Acess_key ='1179990319204425728-sBcmhwklbhvD7sWlrHNJgmCTPLDL8t'
Acess_key_secret ='UwJgDszVX07WvaDAT68iHDplDk0LnBfgi9v8mMEWG8U64'

auth = tweepy.OAuthHandler(consumer_key,consumer_key_secret)

auth.set_access_token(Acess_key,Acess_key_secret)

api = tweepy.API(auth)

public_tweets = api.search('IndVsSA')

countpos,countneg,countNetural =0,0,0
for i in public_tweets:
    # print(i.text)
    analysis = TextBlob(i.text)

    if analysis.sentiment[0]>0:
        # print('Postive'.center(50,'*'))
        countpos+=1
    elif analysis.sentiment[0]<0:
        # print('Negative'.center(50,'*'))
        countneg += 1

    else:
        # print('Netural'.center(50,'*'))
        countNetural +=1

print(f"Postive {countpos} , Negative {countneg} , Netural {countNetural}")


