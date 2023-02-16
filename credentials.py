import requests
import schedule
import time


def send_message():
    resp = requests.post('http://textbelt.com/text', {
        'phone': "5005005",
        'message': "good morning",
        'key': "textbelt"
    })

    print(resp.json())

schedule.every().day.at('06:00').do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)