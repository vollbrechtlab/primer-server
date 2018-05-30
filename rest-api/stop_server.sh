#!/bin/bash
pids=`ps aux | grep primer-server-rest-api-deamon | cut -f2-5 -d' '`
echo $pids | xargs  kill
