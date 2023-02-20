# Lab #1 – KENG + OTGEN CLI + CONTAINER LAB + FRR DUT + BGP

## Description
This lab introduces the concept of Network Topology Emulation via the Container Lab software. This software is in charge of container orchestration (similar to Docker Compose) and also takes care of the underlying network connections (equivalent to creating virtual point-to-point Ethernet interfaces).
This lab uses OTGEN CLI (OTG API Client) to control the KENG Commercial Edition (OTG Test Tool) which is utilized to send raw traffic through a FRR DUT. This lab consists of 1x Ixia-c Controller container, 2x Ixia-c Traffic Engine containers, and 1x FRR container.


## Prerequites 
None! All files and images are included.

## LAB Diagram
![alt text](https://github.com/open-traffic-generator/otg-examples/blob/main/docker-compose/cpdp-frr/diagram.png "Lab Topology")
-

## Network Diagram
![alt text](https://github.com/open-traffic-generator/otg-examples/blob/main/docker-compose/cpdp-frr/ip-diagram.png "Network Topology")

## Start Lab1
- This test drive already Cloned the repo and has all the needed files.

Create Lab topology using Containerlab
```html
cd keng-td/keng/lab1
``` 
```html
  sudo containerlab deploy -t lab1-clab-topology.yml 
```

- Check running containers
```html
docker ps
```

### Lab1: Send undirectional traffic: Port-1 to Dut to Port-2
- Use otgen cli to execute the test with the updated MAC addresses and the IP addresses we got fron the dynamic traffic flows.
```html
source lab1-test-unidirectional.sh

``` 

- Verify results;  1000 frames sent and 1000 recieved.
-
![keng-otg-lab1](https://user-images.githubusercontent.com/13612422/220150196-af800f6d-7bd8-42fb-a884-412add793c1f.png)
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
- [OTG-Example] :https://github.com/open-traffic-generator/otg-examples/tree/main/docker-compose/cpdp-frr
