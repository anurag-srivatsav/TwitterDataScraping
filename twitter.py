from ntscraper import Nitter
scraper = Nitter(log_level = 1,skip_instance_check= False)
tweets = scraper.get_tweets("AnuragSrivatsa4",mode="user",number=10)
from pprint import pprint
pprint(tweets['tweets'])
print()

tweets['tweets']

elon_info = scraper.get_profile_info(username="AnuragSrivatsa4")
pprint(elon_info)
data
import pandas as pd
df = pd.DataFrame(data)
df.head()

import pandas as pd
scraper = Nitter()
def create_tweets_dataset(username,no_of_tweets):
    tweets = scraper.get_tweets(username,mode="user",number=no_of_tweets)
    data = {
        'link':[],
        'text':[],
        'user':[],
        'likes':[],
        'quotes':[],
        'retweets':[],
        'comments':[]
    }

    for tweet in tweets['tweets']:
        data['link'].append(tweet['link'])
        data['text'].append(tweet['text'])
        data['user'].append(tweet['user']['name'])
        data['likes'].append(tweet['stats']['likes'])
        data['quotes'].append(tweet['stats']['quotes'])
        data['retweets'].append(tweet['stats']['retweets'])
        data['comments'].append(tweet['stats']['comments'])
    df = pd.DataFrame(data)
    df.to_csv(username+"_tweets_data.csv")


create_tweets_dataset("MrBeast",10)

