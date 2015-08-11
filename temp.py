# -*- coding: utf-8 -*-
import os
import sys
import time
from os.path import join, dirname

from twilio.rest import TwilioRestClient
from dotenv import load_dotenv

from twython import Twython

if sys.platform == 'darwin':
    import fake_sensor as sensor
else:
    import sensor

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

TEMP_THRESHOLD = 149.0 # farenheit
STEP_VALUE = 5.0

#Twillio Information
TWILIO_SID = os.environ.get('TWILIO_SID')
TWILIO_SECRET = os.environ.get('TWILIO_SECRET')
to_phone = os.environ.get('TO_PHONE')

try:
    to_phone2 = os.environ.get('TO_PHONE')
except ValueError:
    to_phone2 = None


from_phone = os.environ.get('FROM_PHONE')

#Twitter Information
consumer_key = os.environ.get('TWITTER_CONSUMER_KEY')
consumer_secret = os.environ.get('TWITTER_CONSUMER_SECRET')
access_key = os.environ.get('TWITTER_ACCESS_KEY')
access_secret = os.environ.get('TWITTER_ACCESS_SECRET')

def main():
    dummy, start_temp = sensor.read_temp()
    last_step = temp_f = start_temp  #initial value

    while True:
        temp_c, temp_f = sensor.read_temp()
        print(temp_f)
        time.sleep(1)

        if temp_f - last_step > STEP_VALUE:
            last_step = temp_f
            tweet_temp(temp_f)

        if temp_f > TEMP_THRESHOLD:
            text_temp(TEMP_THRESHOLD)
            exit(1)


def text_temp(temperature):
    msg = u'Solar oven has reached {}\xb0 f'.format(temperature)
    print "texting"

    print TWILIO_SID

    client = TwilioRestClient(TWILIO_SID,TWILIO_SECRET)
    client.messages.create(to=to_phone, from_=from_phone, body=msg)
    
    if to_phone2 is not None:
        client.messages.create(to=to_phone2, from_=from_phone, body=msg)


def tweet_temp(temperature):
    print "tweeting"
    status_msg = u'Current solar oven temperature = {} \xb0 f'.format(temperature)
    api = Twython(consumer_key, consumer_secret, access_key, access_secret)
    api.update_status(status=status_msg)


if __name__=="__main__":
    main()
