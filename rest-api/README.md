# Primer Server REST API

## Introduction

server.py is REST API for primerDAFT.
It uses a separate thread for each task request.

## Setup
```shell
# Give permission to the scripts
chmod +x scripts/*.sh

# Install virtual environment if not yet
sudo pip3 install virtualenv

# Create a virtual environment
virtualenv -p python3 venv

# Install packages
venv/bin/pip3 install -r requirements.txt
```

## Useage
```shell
# run server as gunicorn deamon
scripts/start_server.sh

# stop gunicorn deamon
scripts/stop_server.sh
```

## Development
```shell
source venv/bin/activate
python3 server.py
```
