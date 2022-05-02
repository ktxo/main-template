#!/usr/bin/env bash

APP_HOME="/tmp/main-template"

cd ${APP_HOME}
[ $? -ne 0 ] && echo "ERROR: Cannot change to APP_HOME=${APP_HOME}. Aborting" && exit

echo "Using APP_HOME=${APP_HOME}"
./main_template -c config.json -l logging.json $*
