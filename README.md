# google-form-submission

## Requires

yarn

python 3.8

poetry

pyenv (option to use the version in .python-version automatically)

## local dev

poetry install

poetry shell

sls wsgi serve -p 8000


## deploy

yarn install

setup the required parameters in System Manager Parameter Store

/google-form-submission/${self:provider.stage}/teams_url

/google-form-submission/${self:provider.stage}/apikey

e.g. /google-form-submission/dev/teams_url

e.g. /google-form-submission/someone/teams_url


sls deploy

or 

AWS_PROFILE=someone sls deploy --stage someone
