#!/bin/bash -xe
python3.8 -m venv keng
source ./keng/bin/activate
pip install snappi --quiet
LabDir="/home/$USER/keng-td/ixia-c"
LabId="lab2"
TrafficEngine1SrcMac=$(jq .links[0].a.mac $LabDir/$LabId/clab-Ixia-c-DUT-FRR/topology-data.json --raw-output)
TrafficEngine1DstMac=$(jq .links[0].z.mac $LabDir/$LabId/clab-Ixia-c-DUT-FRR/topology-data.json --raw-output)
TrafficEngine2SrcMac=$(jq .links[1].a.mac $LabDir/$LabId/clab-Ixia-c-DUT-FRR/topology-data.json --raw-output)
TrafficEngine2DstMac=$(jq .links[1].z.mac $LabDir/$LabId/clab-Ixia-c-DUT-FRR/topology-data.json --raw-output)
sed -i "s/00:AA:00:00:01:00/$TrafficEngine1SrcMac/g" $LabDir/$LabId/$LabId-test-bidirectional.py
sed -i "s/00:AA:00:00:02:00/$TrafficEngine1DstMac/g" $LabDir/$LabId/$LabId-test-bidirectional.py
sed -i "s/00:AA:00:00:03:00/$TrafficEngine2SrcMac/g" $LabDir/$LabId/$LabId-test-bidirectional.py
sed -i "s/00:AA:00:00:04:00/$TrafficEngine2DstMac/g" $LabDir/$LabId/$LabId-test-bidirectional.py
python $LabDir/$LabId/$LabId-test-bidirectional.py
deactivate