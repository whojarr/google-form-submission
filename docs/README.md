# Setups

[Microsoft Teams - Webhook](#webhook)

[Google Forms - App Script](#appscript)

[AWS System Manager - Parameter Store](#awsssm)


## <a name="webhook">Microsoft Teams - Webhook</a>

* Edit the teams channel connectors

<img src="teams_connectors.png" alt="alt text" width="100"/>

* Search for and configure a new webhook

<img src="teams_webhook_add_new.png" alt="alt text" width="400"/>

* Edit an existing Webhook

<img src="teams_webhook_configure_existing.png" alt="alt text" width="400"/>

* Get the webhook URL

<img src="teams_webhook_setting.png" alt="alt text" width="400"/>


## <a name="appscript">Google Forms - App Script</a>

App Script setup to push form questions at the rest api

1. Open the app script editor

<img src="1.png" alt="alt text" width="600"/>

2. Add the <a href="appscript.txt" parent="_top">new script</a> for the current form

<img src="2.png" alt="alt text" width="600"/>

3. Add a trigger on submit to send the data to the api

<img src="3.png" alt="alt text" width="600"/>

<img src="4.png" alt="alt text" width="600"/>

## <a name="awsssm">AWS Parameter Store</a>

<img src="ssm_teams_url.png" alt="alt text" width="600"/>

<img src="ssm_apikey.png" alt="alt text" width="600"/>