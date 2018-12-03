#!/bin/bash
task_name="gunicorn"
pids=`ps ax | grep primer-server-rest-api-deamon | sed 's/^ \+//g' | cut -f1 -d' '`
echo $pids | xargs  kill
