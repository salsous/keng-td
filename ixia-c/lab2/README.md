
# Lab #2 – IXIA-C + SNAPPI + CONTAINER LAB + FRR DUT

## Description
This lab introduces the concept of Network Topology Emulation via the Container Lab software. This software is in charge of container orchestration (similar to Docker Compose) and also takes care of the underlying network connections (equivalent to creating virtual point-to-point Ethernet interfaces).
This lab uses SNAPPI(Test scripts written in snappi, an auto-generated Python module, can be executed against any traffic generator conforming to the Open Traffic Generator API.) to control the free Ixia-c Community Edition (OTG Test Tool) which is utilized to send raw traffic through a FRR DUT. This lab consists of 1x Ixia-c Controller container, 2x Ixia-c Traffic Engine containers, and 1x FRR container.


## Prerequites 

- 1-lab2-DUT-FRR-config1.
- 2-lab2-DUT-FRR-daemons.
- 3-lab2-clab-topology.yml.
- 4- lab2-test-script.py

## Start Lab2
```html
cd ../lab2
sudo containerlab deploy -t lab2-clab-topology.yml 
``` 
- Check running containers
```html
docker ps
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
python lab2-test-script.py
``` 
- Verify results.
- Cleanup Lab
```html
sudo containerlab deploy -t lab2-clab-topology.yml
``` 
- Verify no more running containers
```html
docker ps
```
