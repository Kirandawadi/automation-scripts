#!/bin/bash

todate=$(date +"%Y-%h-%d-%H-%M")
echo $todate > /home/kdn00b/automation/crontest/subdomains.txt

#Notify Discord
python3 /home/kdn00b/automation/crontest/notifier.py

