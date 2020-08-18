import os
import json
from stock_price_alerts_assets import alert_assets
import requests

# python file location, relative and absolute path
# https://automatetheboringstuff.com/chapter8/
# to install module - python3 -m pip install yfinance


base_path = os.getcwd()
manifest_json = "/web/manifest.json"
json_path = os.path.join(base_path + manifest_json)

json_file = open(json_path, "r")
parsed_json = (json.load(json_file))

account_sid_encoded = 'QUM0ZmZjMWY3ZDRmNDhmNzViYmY5NzhkNzM1NzAzNTliNw=='
account_sid = alert_assets.var_str_decoder(account_sid_encoded)
auth_token_encoded = 'MDFiMWU2MDlkNWQ3Mzk3MjZiNWIxOGVlY2MwOTRmMTU='
auth_token = alert_assets.var_str_decoder(auth_token_encoded)

api_key_encoded = 'YnNzaGVsZjQ4djZ0ZmhtYjQ0YzA='
api_key = alert_assets.var_str_decoder(api_key_encoded)


for key, val in parsed_json.items():

    parsed_json[key]['response'] = alert_assets.ticker_price_request(val['stock']['ticker'], api_key, parsed_json)
    alert_assets.send_a_text_message(account_sid, auth_token, parsed_json, key)




