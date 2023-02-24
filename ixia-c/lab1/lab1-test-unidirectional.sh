#!/bin/bash -xe
LabDir="/home/$USER/keng-td/ixia-c"
LabId="lab1"
export OTG_API="https://clab-Ixia-c-DUT-FRR-Ixia-c-Controller:8443"
export OTG_LOCATION_P1="clab-Ixia-c-DUT-FRR-Ixia-c-Traffic-Engine-1:5551"
export OTG_LOCATION_P2="clab-Ixia-c-DUT-FRR-Ixia-c-Traffic-Engine-2:5552"
TrafficEngine1SrcMac=$(jq .links[0].a.mac $LabDir/$LabId/clab-Ixia-c-DUT-FRR/topology-data.json --raw-output)
TrafficEngine1DstMac=$(jq .links[0].z.mac $LabDir/$LabId/clab-Ixia-c-DUT-FRR/topology-data.json --raw-output)
sed -i "s/00:AA:00:00:01:00/$TrafficEngine1SrcMac/g" $LabDir/$LabId/otg-unidirectional.yml
sed -i "s/00:AA:00:00:02:00/$TrafficEngine1DstMac/g" $LabDir/$LabId/otg-unidirectional.yml
otgen run otgen run --insecure --metrics flow --interval 250ms -f otg-unidirectional.yml | \
otgen transform --metrics flow --counters frames | \
otgen display --mode table
