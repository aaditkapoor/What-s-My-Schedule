from flask import Flask, request
from chatbot.chat import *
from chatbot.binder import *
import requests

app = Flask(__name__)

FB_API_URL = 'https://graph.facebook.com/v4.0/me/messages'
VERIFY_TOKEN = 'facebook_messenger_python_token'
PAGE_ACCESS_TOKEN = 'EAAQSnO4XhnEBAAVSdzi6lzRkeaw4e9QJuaR32yE3CZBiG6neZCHXFEPm92BDmgFCf97iWNDCdcsh1ZCbEosheDKg1NdRZAWaDYbAGi1bFXufnW0AUyKcRsWAKsoezwD7XaTP4iroPEpeeZANXxYxLYsirAB4ceoiq0uAfSaZCVZC1qTlV3ZAoywZA'


def get_bot_response(message, sender_id):
    """
        perform parsing here
    """
    chat = Chat(message,sender_id)
    chat.parse()
    response = chat.getParsedMessage()
    assert
    return response


def verify_webhook(req):
    if req.args.get("hub.verify_token") == VERIFY_TOKEN:
        return req.args.get("hub.challenge")
    else:
        return "incorrect"

def respond(sender, message):
    """Formulate a response to the user and
    pass it on to a function that sends it."""
    response = get_bot_response(message, sender)
    send_message(sender, response)


def is_user_message(message):
    """Check if the message is a message from the user"""
    return (message.get('message') and
            message['message'].get('text') and
            not message['message'].get("is_echo"))


@app.route("/webhook", methods=['GET','POST'])
def listen():
    """This is the main function flask uses to 
    listen at the `/webhook` endpoint"""
    if request.method == 'GET':
        return verify_webhook(request)

    if request.method == 'POST':
        payload = request.json
        print(payload)

        event = payload['entry'][0]['messaging']
        for x in event:
            if is_user_message(x):
                text = x['message']['text']
                sender_id = x['sender']['id']
                print(text, sender_id)
                respond(sender_id, text)

        return "ok"

def send_message(recipient_id, text):
    """Send a response to Facebook"""
    payload = {
        "messaging_type": "RESPONSE",
        'message': {
            'text': text
        },
        'recipient': {
            'id': recipient_id
        },
    }

    auth = {
        'access_token': PAGE_ACCESS_TOKEN
    }

    response = requests.post(
        FB_API_URL,
        params=auth,
        json=payload
    )

    return response.json()