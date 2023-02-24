#!/bin/bash -xe
LabDir="/home/$USER/keng-td/keng"
LabId="lab2"
export OTG_API="https://localhost:8443"
#
curl -k "${OTG_API}/config" -H "Content-Type: application/json" -d @$LabDir/$LabId/otg-config.json
