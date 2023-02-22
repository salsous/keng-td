#!/bin/bash -xe
python3.8 -m venv keng
source ./keng/bin/activate
pip install snappi
LabDir="/home/centos/keng-td/ixia-c"
LabId="lab2"
TrafficEngine1SrcMac=$(jq .links[0].a.mac $LabDir/$LabId/clab-Ixia-c-DUT-FRR/topology-data.json --raw-output)
TrafficEngine1DstMac=$(jq .links[0].z.mac $LabDir/$LabId/clab-Ixia-c-DUT-FRR/topology-data.json --raw-output)
sed -i "s/00:AA:00:00:01:00/$TrafficEngine1SrcMac/g" $LabDir/$LabId/$LabId-test-unidirectional.py
sed -i "s/00:AA:00:00:02:00/$TrafficEngine1DstMac/g" $LabDir/$LabId/$LabId-test-unidirectional.py
python $LabDir/$LabId/$LabId-test-unidirectional.py
deactivate