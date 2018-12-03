#!/bin/bash
task_name="gunicorn"
pids=`ps ax | grep $task_name | cut -f1 -d' '`
echo $pids | xargs  kill
