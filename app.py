from github_webhook import Webhook
from flask import Flask
from github import Github
import os
import json

secret = os.environ.get('SECRET')
app = Flask(__name__)
webhook = Webhook(app, '/postreceive', secret)
g = Github(secret)

print(secret)

@app.route("/")
def hello_world():
	print('test')
    return "Hello, World!"

@webhook.hook("pull_request")
def on_pull_request(response):
	print("{0}".format(response))
	data = json.loads(response)	
#if data.branch == 'gh-pages' and (data.action == 'opened' or data.action == 'reopened'):
	if data.action == 'opened' or data.action == 'reopened':
		pull_request_id = data.number
		g.get_repo(data.repository.id).get_issue(pull_request_id).create_comment('Hello')

if __name__ == "__main__":
    app.run(host="0.0.0.0")
