import requests
import apikeys # add the nexmo keys in this file
import logging
logging.basicConfig(filename='sms_sender.log',level=logging.DEBUG)

phone_numbers = [] #add phone numbers here!
cleaned_phone_numbers = []

for number in phone_numbers:
    new_number = number.replace("-", "")
    if new_number.startswith("010"):
        new_number = new_number.replace("010", "10", 1)
    if new_number.startswith("82") or new_number.startswith("+82"):
        new_number = new_number.replace("+82", "", 1)
        new_number = new_number.replace("82", "", 1)
    cleaned_phone_numbers.append(new_number)

url = "https://rest.nexmo.com/sms/json"
message = "hello" #add message here
payload = {"api_key": apikey.NEXMO_KEY, "api_secret": apikey.NEXMO_SECRET, "text": message, "from": apikeys.PHONE_NUMBER}
for number in cleaned_phone_numbers:
    payload['to'] = number
    r = requests.get(url, params=payload)
    if not r.json()['messages'][0]['status'] == '0':
        logging.warning("SMS FAILED: {}".format(r.json()))
    else:
        logging.info("success to: {}: INFO: {}".format(number, r.json()))


