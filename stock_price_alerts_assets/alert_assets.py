import base64
import requests
from twilio.rest import Client


def var_str_decoder(str1):
    if type(str1) == str:
        return base64.b64decode(str1).decode("utf-8")
    else:
        print('method variable is not a string.')

def ticker_price_request(ticker, apikey, json):
    url = 'https://finnhub.io/api/v1/quote?symbol=' + ticker + '&token=' + apikey
    r = requests.get(url)
    print(r.json())
    return r.json()

def send_a_text_message(accountsid, authtoken, json, key):
    client = Client(accountsid, authtoken)
    phone_number = list(json[key]['phone_number'].values())[0]
    message = client.messages.create(
        body= 'Hi ' + list(json[key]['phone_number'].keys())[0] + ', this is PyBot. For ' + str(json[key]['stock']['name']) + ', here is the price movement. Day Open: $' + str(json[key]['response']['o']) + ', Day Close: $' + str(json[key]['response']['c']) + ', Day High: $' + str(json[key]['response']['h']) + ', Day Low: $' + str(json[key]['response']['l']),
        from_='+12036543578',
        to= '+1' + str(phone_number)
    )
    print('Hi ' + list(json[key]['phone_number'].keys())[0] + ', this is PyBot. For ' + str(json[key]['stock']['name']) + ', here is the price movement. Day Open: $' + str(json[key]['response']['o']) + ', Day Close: $' + str(json[key]['response']['c']) + ', Day High: $' + str(json[key]['response']['h']) + ', Day Low: $' + str(json[key]['response']['l']))
    print(message.sid)