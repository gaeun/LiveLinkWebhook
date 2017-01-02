# LiveLinkWebhook

# How to use LiveLinkWebhook
1. Deploy the LiveLinkWebhook web app on Heroku
..Clone the LiveLinkWebhook repository to your computer, and [deploy the web app](https://dashboard.heroku.com/apps) on Heroku. Once you create a new app through your dashboard, you'll see instructions on how to deploy using Heroku Git -- just follow them :) Alternatively, follow the instructions [here](https://devcenter.heroku.com/articles/git).

2. Get a Github access token
..Once you've deployed the repo on Heroku, get a Github access token for your organization or account in order to access the Github API. Go to your profile settings, and under "Developer Settings" you can generate personal access tokens.

3. Set up config vars on Heroku
..Set up a config var on Heroku. You can do this via CLI, or under the Settings for your deployed app. The key should be SECRET and the value should be the Github access token you just got.

4. Add a webhook on your Github repo
..Go to Settings -> Webhooks page for the repository you want to hook to LiveLinkWebhook. Under "Payload URL" type in heroku_app_link/postreceive. For example: https://gci-fossasia-webhook.herokuapp.com/postreceive
The Secret should be your Github access token. Choose to select individual events under "Which events would you like to trigger this webhook?", and select "Pull Request" only.
