"""
binds everything together
"""
import random
import requests
import os
from pymessenger.bot import Bot

ACCESS_TOKEN = 'EAAjnZCya6LOoBAPSPKKMFotGW1vSBTFmYPqXDnPNhjhiLPJLZA18In1PrpIe6MbuTrU8dA983u54OB0hrP5W2qNHnW7TUZCxJQIVGUhHiiL3U0uAuZBE1dFZC0bBihCZAQ2EzDwS8LmSP1tZBlXu4G49E88io8UZCM5y63obzFZAdxQDr17iiRLEn'
bot = Bot(ACCESS_TOKEN)


def send_message(recipient_id, response):
    bot.send_text_message(recipient_id, response)
    return True


