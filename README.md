# Primer Server

## Environments
All code is developed and tested on Ubuntu 16.04 and RedHat 7.

## Pre-setup
### UI
Install a web server and allow .htaccess

#### Enable the rewrite mod in apache2
cd /etc/apache2/mods-enabled/
sudo ln -s ../mods-available/rewrite.load .

#### Enable the rewrite mod in virtualhost for the right directory
<Directory "$Directory$">
     AllowOverride All
</Directory>


### REST API Server
1. Install python3/pip3
2. Install virtual environment

### etc.
Run `chmod +x *.sh rest-api/*.sh`

## Setup UI
`sudo ./deploy_ui.sh $version`. For example `sudo .deploy_ui.sh 2.2.4`


## Setup REST API Server
```
cd rest-api
./setup_env.sh
cd ..
```
## Run REST API server
`./start_server.sh $version`. For example `./start_server.sh 1.0.4`

## Stop REST API server
`./stop_server.sh $version`. For example, `./stop_server.sh 1.0.4`
