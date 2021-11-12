# google-form-submission

https://github.com/whojarr/google-form-submission/

Contact: David Hunter dhunter@digitalcreation.co.nz

Copyright (C) 2021 Digital Creation Ltd

For license information, see LICENSE


## Requires

serverless framework [https://www.serverless.com/](https://www.serverless.com/)

yarn [https://classic.yarnpkg.com/en/](https://classic.yarnpkg.com/en/)

python 3.8 (i use pyenv below to meet this requirement)

poetry [https://python-poetry.org/](https://python-poetry.org/)

pyenv [https://github.com/pyenv/pyenv](https://github.com/pyenv/pyenv) (option to use the version in .python-version automatically)

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
