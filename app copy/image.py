import json
import requests
def send2(msg,id):
    url = "https://aiubanik.pagekite.me/1"

    payload = json.dumps({
        "Chat_Received": msg,
        "Response": "Image Template",
        "Sender_ID": id,
    })
    headers = {
        'Authorization': 'Bearer DWSBJO5BHGAXCYJ7HOGVK5K6VC6CRHXG',
        'Content-Type': 'application/json',
        'Cookie': 'csrftoken=aw8R0cYrS19k1VLi1TdvfMYDIVZUFESu'
    }

    respons = requests.request("POST", url, headers=headers, data=payload)