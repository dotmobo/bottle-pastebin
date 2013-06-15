# bottle-pastebin

An encrypted and anonymous PasteBin based on the python web framework named Bottle, distributed under the terms of GPL License (http://www.gnu.org/licenses/gpl.html).
* All pastes are AES256 encrypted.
* All AES256 keys are SHA256 encrypted.

## Install
* Install python3 and postgresql
* Install the application and all dependencies with "python3 setup.py develop"
* Create a postgres database
* Configure the config.yaml file
* Run "python3 database.py" to create tables
* Create an hourly cron job with the command "python3 cron.py" to delete the expired pastes

## Run
* Run the server with the command "python3 server.py"
* Go to http://localhost:8080

## Production
* Use an HTTPS apache (or nginx) server to protect the sent data
