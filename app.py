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
	if data['action'] == 'opened' or data['action'] == 'reopened':
		pull_request_id = data['number']
		page_url = 'https://{0}.github.io/{1}'.format(data['sender']['login'], data['repository']['name'])
		g.get_repo(data['repository']['id']).get_issue(pull_request_id).create_comment(page_url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
