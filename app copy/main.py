from flask import Flask, request
import requests
from wit import Wit
from aitemplate import aitemp
from text import send
from image import send2
from Templates import send1, temp, quick1, quick2, audio, text_msg
application = Flask(__name__)

# This is page access token that you get from facebook developer console.
PAGE_ACCESS_TOKEN = 'EAARJC5uL8NcBABKtN7qHifC9mn8zse1gfmOqBB2JeGTqFgekZCZBuFQcGnZCHGejgZBphZCegHZCqSq8P86tKRygS8mqcRrG8cvtA7iran4OiIfK5bZCh0fjSdB8pyL2n1MPa4ZBXXZCO0qIRo2yRXCMUDBV2NsouTHqwcDiOO2sbN9EwZCoVQd7bGPXKF0Lwo9tgZD'
# This is API key for facebook messenger.
API = "https://graph.facebook.com/v13.0/me/messages?access_token=" + PAGE_ACCESS_TOKEN

import requests

url = "http://aiubanik.pagekite.me/2"

payload = ""
headers = {
    'Authorization': 'Bearer DWSBJO5BHGAXCYJ7HOGVK5K6VC6CRHXG',
    'Cookie': 'csrftoken=aw8R0cYrS19k1VLi1TdvfMYDIVZUFESu'
}

response = requests.request("GET", url, headers=headers, data=payload)
r1 = response.json()

Q1 = r1[0]["web_url_1"]
Q2 = r1[0]["web_url_2"]
Q3 = r1[0]["text_response_1"]
Q4 = r1[0]["text_response_2"]
Q5 = r1[0]["audio"]
Q6 = r1[0]["image_1"]
Q7 = r1[0]["image_2"]
Q8 = r1[0]["Flight_Book"]
Q9 = r1[0]["Hotel_Book"]
Q10 = r1[0]["Tourist_Place"]

# This function use for verify token with facebook webhook. So we can verify our flask app and facebook are connected.

# message_text = "I want to fly to Dhaka"


wit_access_token = "27CKIZXSWU3T66YZVHYWLPZVQRGHJ6XN"
client = Wit(access_token=wit_access_token)


# message_text = "I want to fly to Dhaka"


def wit_response(message_text):
    resp = client.message(message_text)

    entity = None
    Shrug = None
    value = None

    try:
        entity = list(resp['entities'])[0]
        value = resp['entities'][entity][0]['resolved']['values'][0]['name']
        Shrug = list(resp['intents'])[0]['name']
    except:
        pass

    return (entity, value, Shrug)


@application.route("/", methods=['GET'])
def fbverify():
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "hello":
            return "Verification token missmatch", 403
        return request.args['hub.challenge'], 200
    return "Hello world", 200


# This function return response to facebook messenger.


@application.route("/", methods=['POST'])
def fbwebhook():
    data = request.get_json()
    print(data)
    try:
        # Read messages from facebook messanger.
        message = data['entry'][0]['messaging'][0]['message']
        sender_id = data['entry'][0]['messaging'][0]['sender']['id']
        # Here we get message text and check specific text so we can send response specificaly.
        messaging_text = message['text']
        msg = message['text']
        id = sender_id
        entity, value, Shrug = wit_response(messaging_text)
        if 'Age' in list(message['text'].split(" ")):
            send(msg,id)
            m = "Tell your Birthyear"
            text_msg(m,id)
        elif 'age' in list(message['text'].split(" ")):
            send(msg, id)
            m = "Tell your Birthyear"
            text_msg(m,id)
        elif Shrug == 'Flight_Book':
            send(msg, id)
            m = Q8 + " {0}".format(str(value))
            text_msg(m, id)
        elif Shrug == 'Hotel_Book':
            send(msg, id)
            m = Q9 + " {0}".format(str(value))
            text_msg(m, id)
        elif Shrug == 'tourist_place':
            send(msg, id)
            m = Q10 + " {0}".format(str(value))
            text_msg(m, id)
        elif message['text'] == "Carry on":
            send1(msg,id,Q1,Q2,Q6,Q7)
        # here we send button response.
        elif message['text'] == "Need other help":
            temp(msg,id)
        # Here we send quick reply response.
        elif message['text'] == "more":
            T = "What do you want:"
            quick1(msg, id,T)
        # Here we send simple text response.
        elif message['text'] == "hello":
            T = Q4
            quick2(msg, id, T)
        elif message['text'] == "hi":
            send(msg,id)
            m = Q3
            text_msg(m,id)
        # Here we send image response.
        elif Shrug == None and int(message['text']) > 999:
            send2(msg, id)
            id = sender_id
            aitemp(msg,id)
        # audio
        elif message['text'] == "Yes":
           send(msg,id)
           img = Q5
           audio(id,img)
        elif Shrug == None and int(message['text']) < 1000:
            send(msg,id)
            m = "Invalid Number"
            text_msg(m, id)

    except:
        # Here we are store the file to our server who send by user from facebook messanger.
        try:
            mess = data['entry'][0]['messaging'][0]['message']['attachments'][0]['payload']['url']
            print("for url-->", mess)
            json_path = requests.get(mess)
            filename = mess.split('?')[0].split('/')[-1]
            open(filename, 'wb').write(json_path.content)
        except:
            print("Noot Found-->")

    return "ok", 200


