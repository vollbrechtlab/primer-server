# Primer Server

## Environments
All code is developed and tested on Ubuntu 16.04 and RedHat 7.

## UI Setup
Install apache2 and allow .htaccess

### Enable the rewrite mod in apache2
```
cd /etc/apache2/mods-enabled/
sudo ln -s ../mods-available/rewrite.load .
```

### Enable the rewrite mod in virtualhost for the right directory
`sudo nano /etc/apache2/sites/available/000-default.conf`

```
<Directory "$Directory$">
     AllowOverride All
</Directory>
```

`sudo service apache2 restart`

## Deploy UI
`sudo ./deploy_ui.sh`

## REST API Server Setup
Follow instructions on `rest-api/readme.md`

## Run REST API Server
`./start_server.sh`.

## Stop REST API Server
`./stop_server.sh`.
