#!/bin/bash
echo stopping server v$1
pids=`ps ax | grep primer-server-rest-api-deamon-v${1} | cut -c2-5`
pid=${pids:0:4}
echo killing ${pid}
kill $pid
