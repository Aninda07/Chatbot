import requests
import json
PAGE_ACCESS_TOKEN = 'EAARJC5uL8NcBABKtN7qHifC9mn8zse1gfmOqBB2JeGTqFgekZCZBuFQcGnZCHGejgZBphZCegHZCqSq8P86tKRygS8mqcRrG8cvtA7iran4OiIfK5bZCh0fjSdB8pyL2n1MPa4ZBXXZCO0qIRo2yRXCMUDBV2NsouTHqwcDiOO2sbN9EwZCoVQd7bGPXKF0Lwo9tgZD'
# This is API key for facebook messenger.
API = "https://graph.facebook.com/v13.0/me/messages?access_token=" + PAGE_ACCESS_TOKEN

def aitemp(msg,id):
    url1 = "https://graph.facebook.com/5511698038895330?fields=first_name,last_name,profile_pic&access_token=EAARJC5uL8NcBABKtN7qHifC9mn8zse1gfmOqBB2JeGTqFgekZCZBuFQcGnZCHGejgZBphZCegHZCqSq8P86tKRygS8mqcRrG8cvtA7iran4OiIfK5bZCh0fjSdB8pyL2n1MPa4ZBXXZCO0qIRo2yRXCMUDBV2NsouTHqwcDiOO2sbN9EwZCoVQd7bGPXKF0Lwo9tgZD>"

    payload1 = ""
    headers1 = {
        'Authorization': 'Bearer EAARJC5uL8NcBABKtN7qHifC9mn8zse1gfmOqBB2JeGTqFgekZCZBuFQcGnZCHGejgZBphZCegHZCqSq8P86tKRygS8mqcRrG8cvtA7iran4OiIfK5bZCh0fjSdB8pyL2n1MPa4ZBXXZCO0qIRo2yRXCMUDBV2NsouTHqwcDiOO2sbN9EwZCoVQd7bGPXKF0Lwo9tgZD'
    }

    response1 = requests.request("GET", url1, headers=headers1, data=payload1)
    r1 = response1.json()
    s2 = r1['first_name']
    url2 = "https://age-generator.onrender.com/myapi/"

    payload2 = json.dumps({
        "Name": s2,
        "Birth_year": msg
    })
    headers2 = {
        'Authorization': 'Bearer EAARJC5uL8NcBABKtN7qHifC9mn8zse1gfmOqBB2JeGTqFgekZCZBuFQcGnZCHGejgZBphZCegHZCqSq8P86tKRygS8mqcRrG8cvtA7iran4OiIfK5bZCh0fjSdB8pyL2n1MPa4ZBXXZCO0qIRo2yRXCMUDBV2NsouTHqwcDiOO2sbN9EwZCoVQd7bGPXKF0Lwo9tgZD',
        'Content-Type': 'application/json'
    }
    response2 = requests.request("POST", url2, headers=headers2, data=payload2)

    headers3 = {
        'Authorization': 'Bearer EAARJC5uL8NcBABKtN7qHifC9mn8zse1gfmOqBB2JeGTqFgekZCZBuFQcGnZCHGejgZBphZCegHZCqSq8P86tKRygS8mqcRrG8cvtA7iran4OiIfK5bZCh0fjSdB8pyL2n1MPa4ZBXXZCO0qIRo2yRXCMUDBV2NsouTHqwcDiOO2sbN9EwZCoVQd7bGPXKF0Lwo9tgZD'
    }
    payload7 = ""

    response = requests.request("GET", url2, headers=headers3, data=payload7)
    T = response.json()
    Age = T[-1]["set_attributes"]["age"]
    Age = str(Age)
    url11 = "https://graph.facebook.com/5511698038895330?fields=first_name,last_name,profile_pic&access_token=EAARJC5uL8NcBABKtN7qHifC9mn8zse1gfmOqBB2JeGTqFgekZCZBuFQcGnZCHGejgZBphZCegHZCqSq8P86tKRygS8mqcRrG8cvtA7iran4OiIfK5bZCh0fjSdB8pyL2n1MPa4ZBXXZCO0qIRo2yRXCMUDBV2NsouTHqwcDiOO2sbN9EwZCoVQd7bGPXKF0Lwo9tgZD>"

    payload11 = ""
    headers11 = {
        'Authorization': 'Bearer EAARJC5uL8NcBABKtN7qHifC9mn8zse1gfmOqBB2JeGTqFgekZCZBuFQcGnZCHGejgZBphZCegHZCqSq8P86tKRygS8mqcRrG8cvtA7iran4OiIfK5bZCh0fjSdB8pyL2n1MPa4ZBXXZCO0qIRo2yRXCMUDBV2NsouTHqwcDiOO2sbN9EwZCoVQd7bGPXKF0Lwo9tgZD'
    }

    response1 = requests.request("GET", url11, headers=headers11, data=payload11)
    r1 = response1.json()

    s1 = r1['profile_pic']
    img_data = requests.get(s1).content
    with open('image_name.png', 'wb') as handler:
        handler.write(img_data)
    url4 = "https://5e5e-103-85-159-72.in.ngrok.io/myapi/"

    payload4 = {'Description': '   You are ' + Age}
    files = [
        ('Picture', ('image_name.png', open(
            'image_name.png', 'rb'),
                     'image/png'))
    ]
    headers4 = {
        'Authorization': 'Bearer EAARJC5uL8NcBABKtN7qHifC9mn8zse1gfmOqBB2JeGTqFgekZCZBuFQcGnZCHGejgZBphZCegHZCqSq8P86tKRygS8mqcRrG8cvtA7iran4OiIfK5bZCh0fjSdB8pyL2n1MPa4ZBXXZCO0qIRo2yRXCMUDBV2NsouTHqwcDiOO2sbN9EwZCoVQd7bGPXKF0Lwo9tgZD'
    }

    response4 = requests.request("POST", url4, headers=headers4, data=payload4, files=files)
    url5 = "https://5e5e-103-85-159-72.in.ngrok.io/myapi/"

    payload5 = ""
    headers5 = {
        'Authorization': 'Bearer EAARJC5uL8NcBABKtN7qHifC9mn8zse1gfmOqBB2JeGTqFgekZCZBuFQcGnZCHGejgZBphZCegHZCqSq8P86tKRygS8mqcRrG8cvtA7iran4OiIfK5bZCh0fjSdB8pyL2n1MPa4ZBXXZCO0qIRo2yRXCMUDBV2NsouTHqwcDiOO2sbN9EwZCoVQd7bGPXKF0Lwo9tgZD'
    }
    response5 = requests.request("GET", url5, headers=headers5, data=payload5)
    Ans = response5.json()
    A1 = Ans[-1]["set_attributes"]["Picture"]
    A1 = str(A1)
    request_body = {
        "recipient": {
            "id": id
        },
        "message": {
            "attachment": {
                "type": "image",
                "payload": {
                    "url": A1,
                    "is_reusable": True
                }
            }
        }
    }
    response = requests.post(API, json=request_body).json()
    return response


