from github_webhook import Webhook
from flask import Flask
from github import Github
import os
import sys
import json

secret = os.environ.get('SECRET')
app = Flask(__name__)
webhook = Webhook(app, '/postreceive', secret)
g = Github(secret)

@app.route("/")
def hello_world():
    return "Hello, World!"

@webhook.hook("pull_request")
def on_pull_request(data):
	print(data['number'])
#if data.branch == 'gh-pages' and (data.action == 'opened' or data.action == 'reopened'):
	if data['action'] == 'opened' or data['action'] == 'reopened':
		pull_request_id = data['number']
		print('test')
		print(pull_request_id)
		g.get_repo(data['repository']['id']).get_issue(pull_request_id).create_comment('Hello')

if __name__ == "__main__":
    app.run(host="0.0.0.0")
