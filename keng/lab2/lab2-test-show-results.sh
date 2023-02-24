#!/bin/bash -xe
LabDir="/home/$USER/keng-td/keng"
LabId="lab2"
export OTG_API="https://localhost:8443"
#

watch -n 1 "curl -sk \"${OTG_API}/results/metrics\" -X POST -H 'Content-Type: application/json' -d '{ \"choice\": \"flow\" }'"
