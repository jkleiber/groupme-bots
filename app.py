# RESOURCE: http://www.apnorton.com/blog/2017/02/28/How-I-wrote-a-Groupme-Chatbot-in-24-hours/
# This code is also based on BenDMyers' boilerplate groupme bot, found here: https://github.com/BenDMyers/Boilerplate_GroupMe_Bot

# IMPORTS
import json
import os

from flask import Flask, request
from src.snek.snek import Snek
from urllib.parse import urlencode
from urllib.request import Request, urlopen

app = Flask(__name__)

# Bot IDs
snek_id = "b0fc5b9a00b6b72c1ba2f314c8"

# Bots
snek = Snek(snek_id)

# Called whenever the app's callback URL receives a POST request
# That'll happen every time a message is sent in the group
@app.route('/', methods=['POST'])
def webhook():
	# 'message' is an object that represents a single GroupMe message.
	message = request.get_json()

	snek.sendSnek(message)

	return "ok", 200