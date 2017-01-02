from github_webhook import Webhook
from flask import Flask

app = Flask(__name__)  # Standard Flask app
webhook = Webhook(app) # Defines '/postreceive' endpoint

@app.route("/")        # Standard Flask endpoint
def hello_world():
    return "Hello, World!"

@webhook.hook("pull_request")
def on_pull_request(data):
    print("{0}".format(data))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
