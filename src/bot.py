"""
 General class for a bot. Use this to send messages and perform other actions
"""

# IMPORTS
import json
import os

from flask import Flask, request
from urllib.parse import urlencode
from urllib.request import Request, urlopen

class Bot:

	def __init__(self, ID: str):
		""" Make a new Bot """
		self.bot_id = ID

	def reply(self, msg):
		""" Reply to messages """
		url = 'https://api.groupme.com/v3/bots/post'
		data = {
			'bot_id'		: self.bot_id,
			'text'			: msg
		}
		request = Request(url, urlencode(data).encode())
		json = urlopen(request).read().decode()

	def reply_with_image(self, msg: str, imgURL: str):
		""" Reply to groupchat with images """
		url = 'https://api.groupme.com/v3/bots/post'
		urlOnGroupMeService = upload_image_to_groupme(imgURL)
		data = {
			'bot_id'		: self.bot_id,
			'text'			: msg,
			'picture_url'	: urlOnGroupMeService
		}
		request = Request(url, urlencode(data).encode())
		json = urlopen(request).read().decode()

	def upload_image_to_groupme(self, imgURL: str):
		""" Uploads image to GroupMe's services and returns the new URL """
		imgRequest = requests.get(imgURL, stream=True)
		filename = 'temp.png'
		postImage = None
		if imgRequest.status_code == 200:
			# Save Image
			with open(filename, 'wb') as image:
				for chunk in imgRequest:
					image.write(chunk)
			# Send Image
			headers = {'content-type': 'application/json'}
			url = 'https://image.groupme.com/pictures'
			files = {'file': open(filename, 'rb')}
			payload = {'access_token': 'eo7JS8SGD49rKodcvUHPyFRnSWH1IVeZyOqUMrxU'}
			r = requests.post(url, files=files, params=payload)
			imageurl = r.json()['payload']['url']
			os.remove(filename)
			return imageurl

	def sender_is_bot(self, message):
		""" Checks whether the message sender is a bot """
		return message['sender_type'] == "bot"