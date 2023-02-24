#!/bin/bash -xe
LabDir="/home/$USER/keng-td/keng"
LabId="lab2"
export OTG_API="https://localhost:8443"
#
curl -k "${OTG_API}/control/protocols" -H "Content-Type: application/json" -d '{"state" : "start"}'
