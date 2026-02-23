#!/usr/bin/env bash
TopDir=/paperstack-working-directory

echo "Start Paperstack server"

if [[ -d ${TopDir} ]]; then
    cd ${TopDir}
    if [[ -d venv ]]; then
        . ./venv/bin/activate
        paperstack-server --host 192.168.11.20 --port 7610
    else
        echo "No python venv found in ${TopDir}, exiting ..."
    fi
else
    echo "Top working directory for paperstack ${TopDir} not found, exiting ..."
fi
