
import requests
import pygsheets

# import var's from vars.py
from vars import *

### Monobank section ###

response = requests.get('https://api.monobank.ua/personal/client-info', headers={'X-Token': x_token})

data = response.json()['accounts']

cards_info = []
for a in data:
    if a['iban'] == iban:
        balance = a['balance']
        cards_info.append(balance)

monobank_result = str(cards_info)[+2:-3]

### Monobank section ###

### Google Sheets section ###

gc = pygsheets.authorize(service_file='./token.json', scopes=('https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'))

wks = gc.open_by_key(gsheets_id).sheet1

wks.update_value(gsheets_cell, monobank_result)

### Google Sheets section ###