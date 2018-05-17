#!/bin/bash
wget localhost:51678/v1/metadata -t 1 -qO- &> /dev/null

if [ $? -eq 0 ]
then
    export ISAWS=1
else
    export ISAWS=0
fi

cd ${PROJECT_ROOT}/lab

if [ -d 'node_modules' ]; then
    echo "npm ready"
else
    echo "unzipping npm dependencies and then installing pm2"
    tar -zvxf /root/node_modules.tar.gz node_modules
    touch .env
    npm install -g pm2
fi

if [ -d 'bower_components' ]; then
    echo "bower_components ready"
else
    echo "unzipping bower_components"
    tar -zvxf /root/bower_components.tar.gz bower_components

fi

if [ -d 'www' ]; then
    echo "www ready"
else
    echo "unzipping www"
    tar -zvxf /root/www.tar.gz www

fi

if [ ! -d "../tmp" ]; then
    mkdir ../tmp
fi

pm2 start lab.config.js --watch

#figure out where we are running
if [ ${ISAWS} -eq 1 ]
then
    while [ ! -f /tmp/die.txt ]
    do
      sleep 2
    done
    cat /tmp/die.txt
else
    bash
fi
