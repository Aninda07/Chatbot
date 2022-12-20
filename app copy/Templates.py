import requests
from flask import Flask, request
import requests
from wit import Wit

application = Flask(__name__)

# This is page access token that you get from facebook developer console.
PAGE_ACCESS_TOKEN = 'EAARJC5uL8NcBABKtN7qHifC9mn8zse1gfmOqBB2JeGTqFgekZCZBuFQcGnZCHGejgZBphZCegHZCqSq8P86tKRygS8mqcRrG8cvtA7iran4OiIfK5bZCh0fjSdB8pyL2n1MPa4ZBXXZCO0qIRo2yRXCMUDBV2NsouTHqwcDiOO2sbN9EwZCoVQd7bGPXKF0Lwo9tgZD'
# This is API key for facebook messenger.
API = "https://graph.facebook.com/v13.0/me/messages?access_token=" + PAGE_ACCESS_TOKEN

def send1(msg,id,Q1,Q2,Q6,Q7):
    import json

    url = "https://aiubanik.pagekite.me/1"

    payload = json.dumps({
        "Chat_Received": msg,
        "Response": "Carousel",
        "Sender_ID": id,
    })
    headers = {
        'Authorization': 'Bearer DWSBJO5BHGAXCYJ7HOGVK5K6VC6CRHXG',
        'Content-Type': 'application/json',
        'Cookie': 'csrftoken=aw8R0cYrS19k1VLi1TdvfMYDIVZUFESu'
    }

    respons = requests.request("POST", url, headers=headers, data=payload)
    request_body = {
        "recipient": {
            "id": id
        },
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                        {
                            "title": "Welcome to easyfashion. Here you can find the best clothing designs for your comfort",
                            "image_url": Q6,
                            "subtitle": "We have the right clothe for everyone.",
                            "default_action": {
                                "type": "web_url",
                                "url": Q1,
                                "webview_height_ratio": "tall",
                            },
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "url": Q1,
                                    "title": "View Website"
                                }, {
                                    "type": "postback",
                                    "title": "Start app",
                                    "payload": "DEVELOPER_DEFINED_PAYLOAD"
                                }
                            ]
                        },
                        {
                            "title": "Welcome to best flight shedules",
                            "image_url": Q7,
                            "subtitle": "We have the right hat for everyone.",
                            "default_action": {
                                "type": "web_url",
                                "url": Q2,
                                "webview_height_ratio": "tall",
                            },
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "url": Q2,
                                    "title": "View Website"
                                }, {
                                    "type": "postback",
                                    "title": "Start app",
                                    "payload": "DEVELOPER_DEFINED_PAYLOAD"
                                }
                            ]
                        }
                    ]
                }
            }
        }
    }
    response = requests.post(API, json=request_body).json()
    return response

def temp(msg,id):
    import json

    url = "https://aiubanik.pagekite.me/1"

    payload = json.dumps({
        "Chat_Received": msg,
        "Response": "template",
        "Sender_ID": id,
    })
    headers = {
        'Authorization': 'Bearer DWSBJO5BHGAXCYJ7HOGVK5K6VC6CRHXG',
        'Content-Type': 'application/json',
        'Cookie': 'csrftoken=aw8R0cYrS19k1VLi1TdvfMYDIVZUFESu'
    }

    respons = requests.request("POST", url, headers=headers, data=payload)
    request_body = {
        "recipient": {
            "id": id
        },
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "button",
                    "text": "You can research by yourselves. Or you directly call us.",
                    "buttons": [
                        {
                            "type": "web_url",
                            "url": "https://www.google.com",
                            "title": "Research on google search engine"
                        },
                        {
                            "type": "web_url",
                            "url": "https://www.youtube.com",
                            "title": "Visit Youtube"
                        },
                        {
                            "type": "phone_number",
                            "title": "Call us",
                            "payload": "01760755706"
                        },
                    ]
                }
            }
        }
    }
    response = requests.post(API, json=request_body).json()
    return response

def quick2(msg,id,T):
    import json

    url = "https://aiubanik.pagekite.me/1"

    payload = json.dumps({
        "Chat_Received": msg,
        "Response": "Quick Reply",
        "Sender_ID": id,
    })
    headers = {
        'Authorization': 'Bearer DWSBJO5BHGAXCYJ7HOGVK5K6VC6CRHXG',
        'Content-Type': 'application/json',
        'Cookie': 'csrftoken=aw8R0cYrS19k1VLi1TdvfMYDIVZUFESu'
    }

    respons = requests.request("POST", url, headers=headers, data=payload)
    request_body = {
        "recipient": {
            "id": id
        },
        "messaging_type": "RESPONSE",
        "message": {
            "text": T,
            "quick_replies": [
                {
                    "content_type": "text",
                    "title": "No",
                    "payload": "<POSTBACK_PAYLOAD>",
                    "image_url": "https://ppd-b2b.de/media/e2/14/6c/1625556103/1254258_gr.jpg"
                }, {
                    "content_type": "text",
                    "title": "Yes",
                    "payload": "<POSTBACK_PAYLOAD>",
                    "image_url": "https://www.flizes.lv/i/color-line-cli859-light-green-25x25.spm.7745-b1.jpeg"
                }
            ]
        }
    }
    response = requests.post(API, json=request_body).json()
    return response
    

def quick1(msg,id,T):
    import json

    url = "https://aiubanik.pagekite.me/1"

    payload = json.dumps({
        "Chat_Received": msg,
        "Response": "Quick Reply",
        "Sender_ID": id,
    })
    headers = {
        'Authorization': 'Bearer DWSBJO5BHGAXCYJ7HOGVK5K6VC6CRHXG',
        'Content-Type': 'application/json',
        'Cookie': 'csrftoken=aw8R0cYrS19k1VLi1TdvfMYDIVZUFESu'
    }

    respons = requests.request("POST", url, headers=headers, data=payload)
    request_body = {
        "recipient": {
            "id": id
        },
        "messaging_type": "RESPONSE",
        "message": {
            "text": T,
            "quick_replies": [
                {
                    "content_type": "text",
                    "title": "Carry on",
                    "payload": "<POSTBACK_PAYLOAD>",
                    "image_url": "https://ppd-b2b.de/media/e2/14/6c/1625556103/1254258_gr.jpg"
                }, {
                    "content_type": "text",
                    "title": "Need other help",
                    "payload": "<POSTBACK_PAYLOAD>",
                    "image_url": "https://www.flizes.lv/i/color-line-cli859-light-green-25x25.spm.7745-b1.jpeg"
                }
            ]
        }
    }
    response = requests.post(API, json=request_body).json()
    return response

def audio(id,img):
    request_body = {
        "recipient": {
            "id": id
        },
        "message": {
            "attachment": {
                "type": "audio",
                "payload": {
                    "url": img,
                    "is_reusable": True
                }
            }
        }
    }
    response = requests.post(API, json=request_body).json()
    return response

def text_msg(m,id):
    request_body = {
        "recipient": {
            "id": id
        },
        "message": {
            "text": m
        }
    }

    response = requests.post(API, json=request_body).json()
    return response

