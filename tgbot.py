import requests
import pprint
token = '6826330942:AAGc1eS6WDuJKGpwNQ2QS-5P5P_AHqX0l58'
main_url = f'https://api.telegram.org/bot{token}'
url = f'{main_url}/getUpdates'

result = requests.get(url)
pprint.pprint(result.json())


messages = result.json()['result']
for message in messages:
    chat_id = message['message']['chat']['id']
    url = f'{main_url}/sendMessage'
    params = {
        'chat_id': chat_id,
        'text': 'Датствуйте'
    }
    result = requests.post(url, params = params)