"""
binds everything together
"""
import random
import requests
import os
from pymessenger.bot import Bot

ACCESS_TOKEN = 'EAAQSnO4XhnEBADtq36iry4WD7CZB8qLROF5CKtuy131iTOXiXsfUtKdZAafW2ZBykimLBpPh29ukuU7VoaIBZBQxJfMKhLgoV178Yvh9kC1ZCm2XecZA0ZAlzx7EZCBvz7bC2XvhDd8Csr3d1EbZChfCZAfGZCZBtEBVCauMr0Mk9WmpNcotkXLZBkuof '
bot = Bot(ACCESS_TOKEN)


def send_message(recipient_id, response):
    bot.send_text_message(recipient_id, response)
    return True

