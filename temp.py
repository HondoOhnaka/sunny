import os
from os.path import join, dirname

from twilio.rest import TwilioRestClient 
from dotenv import load_dotenv

from twython import Twython  

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

#Twillio Information
auth = os.environ.get('TWILIO_SID')
token = os.environ.get('TWILIO_SECRET')
to_phone = os.environ.get('TO_PHONE')
from_phone = os.environ.get('FROM_PHONE')

#Twitter Information
consumer_key = os.environ.get('TWITTER_CONSUMER_KEY')
consumer_secret = os.environ.get('TWITTER_CONSUMER_SECRET')
access_key = os.environ.get('TWITTER_ACCESS_KEY')
access_secret = os.environ.get('TWITTER_ACCESS_SECRET') 


def text_temp(temperature):
    msg = 'Solar oven has reached '+temperature+' F'

    client = TwilioRestClient(auth,token)  
    msg = client.messages.create(to=to_phone, from_=from_phone, body=msg)
    
    
def tweet_temp(temperature):
    api = Twython(consumer_key,consumer_secret, access_key, access_secret)     
    api.update_status(status="Current solar oven temperature = "+temperature+" F")  