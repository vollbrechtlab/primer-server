#!/bin/bash
pids=`ps ax | grep primer-server-rest-api-deamon | cut -f1 -d' '`
echo $pids | xargs  kill
