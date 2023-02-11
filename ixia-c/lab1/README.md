
# Lab #1 – IXIA-C + OTGEN CLI + CONTAINER LAB + FRR DUT

## Description
This lab introduces the concept of Network Topology Emulation via the Container Lab software. This software is in charge of container orchestration (similar to Docker Compose) and also takes care of the underlying network connections (equivalent to creating virtual point-to-point Ethernet interfaces).
This lab uses OTGEN CLI (OTG API Client) to control the free Ixia-c Community Edition (OTG Test Tool) which is utilized to send raw traffic through a FRR DUT. This lab consists of 1x Ixia-c Controller container, 2x Ixia-c Traffic Engine containers, and 1x FRR container.


## Prerequites 
Git clone repo to get all needed files below
- 1- lab1-DUT-FRR-config1.
- 2-lab1-DUT-FRR-daemons.
- 3-lab1-clab-topology.yml.
- 4-OTGEN CLi client

## Lab Topology
![Network-topo1](https://user-images.githubusercontent.com/13612422/218280411-7504d9ce-e6ce-483e-9e8d-ce7791d2edb2.png)


## Network Diagram
![alt text](https://github.com/open-traffic-generator/otg-examples/blob/main/clab/ixia-c-te-frr/ip-diagram.png "Network Topology")

## Start Lab1
- Clone the repo
```html
git clone https://github.com/salsous/keng-td.git
``` 
- Create Lab topology using Containerlab
```html
  cd keng-td/ixia-c/lab1
  sudo containerlab deploy -t lab1-clab-topology.yml 
```

- Check running containers
```html
docker ps
```
- Prepare the OTGEN CLI tool with correct environment parameters
```html
export OTG_API="https://clab-Ixia-c-DUT-FRR-Ixia-c-Controller:8443"
export OTG_LOCATION_P1="clab-Ixia-c-DUT-FRR-Ixia-c-Traffic-Engine-1:5551"
export OTG_LOCATION_P2="clab-Ixia-c-DUT-FRR-Ixia-c-Traffic-Engine-2:5552"
``` 
- Use the JQ tool to parse the output of the Container Lab topology file and extract all the relevant MAC addresses.
```html
TE1SMAC=`cat ./clab-Ixia-c-DUT-FRR/topology-data.json | jq -r '.links[0]["a"].mac'`
TE1DMAC=`cat ./clab-Ixia-c-DUT-FRR/topology-data.json | jq -r '.links[0]["z"].mac'`
```
- Verify that all information has been extracted correctly from the Container Lab topology file.
```html
echo $TE1SMAC
echo $TE1DMAC
``` 
- Use otgen cli to execute the test with the updated MAC addresses and the IP addresses used to create the raw traffic flows.
```html
otgen create flow -s 198.51.100.10 -d 203.0.113.10 -p 80 --rate 1000 --count 1000 --size 512 --smac $TE1SMAC --dmac $TE1DMAC | \
otgen run --insecure --metrics port --interval 250ms | \
otgen transform --metrics port --counters bytes | \
otgen display --mode table
``` 
- Verify results. You should have seen 512000 packets sent and 512000 recieved.
- 
![lab1-results](https://user-images.githubusercontent.com/13612422/218182775-1083eca6-b11a-4ce6-abcb-4fded75e9f19.png)
-
- Cleanup Lab
```html
sudo containerlab destroy -t lab1-clab-topology.yml
``` 
- Verify no more running containers
```html
docker ps
```

## References
- [open-taffic-generator] :https://github.com/open-traffic-generator
- [OTG-Example] :https://github.com/open-traffic-generator/otg-examples/tree/main/clab/ixia-c-te-frr
