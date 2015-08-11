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
auth = os.environ.get('TWILIO_SID')
token = os.environ.get('TWILIO_SECRET')
to_phone = os.environ.get('TO_PHONE')
from_phone = os.environ.get('FROM_PHONE')

#Twitter Information
consumer_key = os.environ.get('TWITTER_CONSUMER_KEY')
consumer_secret = os.environ.get('TWITTER_CONSUMER_SECRET')
access_key = os.environ.get('TWITTER_ACCESS_KEY')
access_secret = os.environ.get('TWITTER_ACCESS_SECRET')

def main():
    start_temp = sensor.read_temp()
    temp_f = start_temp  #initial value

    while True:
        temp_f, temp_c = sensor.read_temp()
        print(temp_f)
        time.sleep(1)

        if temp_f - last_temp > STEP_VALUE:
            tweet_temp(temperature)

        if temp_f > TEMP_THRESHOLD:
            text_temp(TEMP_THRESHOLD)
            exit(1)

        last_temp = temp_f # keep the last value




def text_temp(temperature):
    msg = 'Solar oven has reached {}\xb0 f'.format(temperature)

    client = TwilioRestClient(auth,token)
    client.messages.create(to=to_phone, from_=from_phone, body=msg)


def tweet_temp(temperature):
    status_msg = "Current solar oven temperature = {} \xb0 f".format(temperature)
    api = Twython(consumer_key, consumer_secret, access_key, access_secret)
    api.update_status(status=status_msg)


if __name__=="__main__":
    main()
