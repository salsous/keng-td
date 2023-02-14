# Lab #1 – KENG + OTGEN CLI + CONTAINER LAB + FRR DUT + BGP

## Description
This lab introduces the concept of Network Topology Emulation via the Container Lab software. This software is in charge of container orchestration (similar to Docker Compose) and also takes care of the underlying network connections (equivalent to creating virtual point-to-point Ethernet interfaces).
This lab uses OTGEN CLI (OTG API Client) to control the KENG Commercial Edition (OTG Test Tool) which is utilized to send raw traffic through a FRR DUT. This lab consists of 1x Ixia-c Controller container, 2x Ixia-c Traffic Engine containers, and 1x FRR container.


## Prerequites 
Git clone repo to get all needed files below
- 1- lab1-DUT-FRR-config1.
- 2-lab1-DUT-FRR-daemons.
- 3-lab1-clab-topology.yml.
- 4- OTGEN CLi client.

## LAB Diagram
![alt text](https://github.com/open-traffic-generator/otg-examples/blob/main/docker-compose/cpdp-frr/diagram.png "Lab Topology")
-

## Network Diagram
![alt text](https://github.com/open-traffic-generator/otg-examples/blob/main/docker-compose/cpdp-frr/ip-diagram.png "Network Topology")

## Start Lab1
- Clone the repo
```html
git clone https://github.com/salsous/keng-td.git
``` 
- cd ./keng/lab1
- cat lab1-clab-topology.yml

```html
  sudo containerlab deploy -t lab1-clab-topology.yml 
```

- Check running containers
```html
docker ps
```
- Prepare the OTGEN CLI tool with correct environment parameters
```html
export OTG_API="https://localhost:8443"
otgen --log info run --insecure --file otg.json --json --rxbgp 2x --metrics flow | jq

``` 
- To format output as a table, use the modified command below.
```html
otgen run --insecure --file otg.json --json --rxbgp 2x --metrics flow | otgen transform --metrics flow | otgen display --mode table
``` 

- Verify results.

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
- [OTG-Example] :https://github.com/open-traffic-generator/otg-examples/tree/main/docker-compose/cpdp-frr
