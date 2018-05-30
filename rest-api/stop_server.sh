#!/bin/bash
pids=`ps ax | grep primer-server-rest-api-deamon | cut -f1-2 -d' '`
echo $pids | xargs  kill
