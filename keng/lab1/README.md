# Lab #2A – KENG + OTGEN CLI + CONTAINER LAB + FRR DUT + BGP

## Description
This lab introduces the concept of Network Topology Emulation via the Container Lab software. This software is in charge of container orchestration (similar to Docker Compose) and also takes care of the underlying network connections (equivalent to creating virtual point-to-point Ethernet interfaces).
This lab uses OTGEN CLI (OTG API Client) to control the KENG Commercial Edition (OTG Test Tool) which is utilized to send raw traffic through a FRR DUT. This lab consists of 1x Ixia-c Controller container, 2x Ixia-c Traffic Engine containers, and 1x FRR container.


## Prerequites 
Git clone repo to get all needed files below
- 1- lab2-DUT-FRR-config1.
- 2-lab2-DUT-FRR-daemons.
- 3-lab2-clab-topology.yml.
- 4- lab2-test-script.py.

## Start Lab1
- Clone the repo
```html
git clone https://github.com/salsous/keng-td.git
``` 
- cd ./ixia-c/lab2
- cat lab1-clab-topology.yml

```html
  sudo containerlab deploy -t lab2-clab-topology.yml 
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
TE2SMAC=`cat ./clab-Ixia-c-DUT-FRR/topology-data.json | jq -r '.links[1]["a"].mac'`
TE2DMAC=`cat ./clab-Ixia-c-DUT-FRR/topology-data.json | jq -r '.links[1]["z"].mac'`
``` 
- Verify that all information has been extracted correctly from the Container Lab topology file.
```html
echo $TE1SMAC
echo $TE1DMAC
echo $TE2SMAC
echo $TE2DMAC
``` 
- Execute the test script using the correct MAC addresses and the IP addresses used to create the raw traffic flows.
```html
otgen create flow -s 192.0.2.1 -d 192.0.2.5 -p 80 --rate 100 --count 2000 --size 512 --smac $TE1SMAC --dmac $TE1DMAC | \
otgen run --insecure --metrics port --interval 250ms | \
otgen transform --metrics port --counters bytes | \
otgen display --mode table
``` 
- Verify results.
## References
- [open-taffic-generator] :https://github.com/open-traffic-generator
- [OTG-Example] :https://github.com/open-traffic-generator/otg-examples/tree/main/docker-compose/cpdp-frr
