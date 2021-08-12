#!/bin/bash

date=$(date +"%Y-%h-%d-%H-%M")

#scan the domain
#make aggregated file
#anew with old file
#if any new subdomain found, alert!

cat new_scan | anew google.com > just_found

#Notify Discord if new subdomains found
string=$(cat ./just_found)
if [[ -n "$string" ]]; then
  python3 ./notifier.py   
fi
