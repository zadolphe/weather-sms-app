import requests 
import os
from twilio.rest import Client


account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

client = Client(account_sid, auth_token)
apiKey = os.environ.get('TWILIO_API_KEY')
parameters = {"lat": 51.0447,
"lon": 114.0719,
"appid": apiKey
}
OWM_ENDpoint = "https://api.openweathermap.org/data/2.5/weather"

response = requests.get(url=OWM_ENDpoint, params= parameters)

weatherData = response.json()
will_rain = False
condition_code = weatherData['weather'][0]['id']
main = weatherData['weather'][0]['main']
description = weatherData['weather'][0]['description']


if int(condition_code) < 700:
    will_rain = True

if will_rain:
    #text message to send via SMS
    message = client.messages \
                .create(
                     body=f"Bring an umbrella, today it is: {main}{description}",
                     from_='+19519163503',
                     to='+15877779990'
                 )
else:
    message2 = client.messages \
                .create(
                     body=f"No need for an umbrella, it is: {main} {description}",
                     from_='+19519163503',
                     to='+15877779990'
                 )
