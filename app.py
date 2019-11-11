# RESOURCE: http://www.apnorton.com/blog/2017/02/28/How-I-wrote-a-Groupme-Chatbot-in-24-hours/
# This code is also based on BenDMyers' boilerplate groupme bot, found here: https://github.com/BenDMyers/Boilerplate_GroupMe_Bot

# IMPORTS
import json
import os

from flask import Flask, request
from urllib.parse import urlencode
from urllib.request import Request, urlopen

# Bot imports
from src.projectmanager.projectmanager import ProjectManager
from src.snek.snek import Snek


app = Flask(__name__)

# Bot IDs
pm_id = "0f9731e90b0f5d15fe222b5e5c"#"764cc41f34f6b5ddcfcdc225ca"
snek_id = "b0fc5b9a00b6b72c1ba2f314c8"

# Bots
pm = ProjectManager(pm_id)
snek = Snek(snek_id)

# Called whenever the app's callback URL receives a POST request
# That'll happen every time a message is sent in the group
@app.route('/', methods=['POST'])
def webhook():
    # 'message' is an object that represents a single GroupMe message.
    message = request.get_json()

    # Use your favorite bot here
    # snek.sendSnek(message)

    return "ok", 200

# Called for the project manager bot
@app.route('/projectmanager', methods=['POST'])
def project_manager_webhook():
    # 'message' is an object that represents a single GroupMe message.
    message = request.get_json()

    # respond to users and manage the project
    pm.manage_project(message)

    return "ok", 200

@app.route('/statusreports', methods=['POST'])
def status_report_webhook():
    # Remind everyone in the channel to send status reports
    pm.status_report_reminder()

    return "ok", 200
