"""
entry point of the app where the routes are defined
"""

from flask import Flask, request
import random
import requests
from pymessenger.bot import Bot


app = Flask(__name__)
ACCESS_TOKEN = 'EAAjnZCya6LOoBAIkfgGse0oLcpvTKzviAAhbgbBx9jBdbOMLjjDv51amy2ajT7RSHBfZC809XWZB1Bpl2IbnmtZCeozyiCW0FNkvrLaUIYc4UgcdZAfAZApl5Ydk3vFmjZCxoV55NvzymiOi17RZBVBfm4IlXslNxCmVnmZCZBN5bJ7pEMEk0CPQQL'
VERIFY_TOKEN = 'facebook_messenger_chatbot_schedule_python'
bot = Bot(ACCESS_TOKEN)

@app.route('/webhook', methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        # Before allowing people to message your bot, Facebook has implemented a verify token
        # that confirms all requests that your bot receives came from Facebook.
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    else:
        output = request.get_json()
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                if message.get('message'):
                # Facebook Messenger ID for user so we know where to send response back to
                    recipient_id = message['sender']['id']
                    if message['message'].get('text'):
                        response_sent_text = get_message()
                        send_message(recipient_id, response_sent_text)
                # if user sends us a GIF, photo,video, or any other non-text item
                    if message['message'].get('attachments'):
                        response_sent_nontext = get_message()
                        send_message(recipient_id, response_sent_nontext)


        return "Message Processed"



def verify_fb_token(token_sent):
    #take token sent by facebook and verify it matches the verify token you sent
    #if they match, allow the request, else return an error
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'


def send_message(recipient_id, response):
    #sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"

def get_message():
    sample_responses = ["You are stunning!", "We're proud of you.", "Keep on being you!", "We're greatful to know you :)"]
    return random.choice(sample_responses)
