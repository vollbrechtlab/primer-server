#!/bin/bash
cd v$1
venv/bin/gunicorn -b 0.0.0.0:8001 --workers=2 --access-logfile logs/gunicorn-access.log --error-logfile logs/gunicorn-error.log server:app --daemon --name=primer-server-rest-api-deamon-v$1
cd ..
