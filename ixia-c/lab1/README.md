
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
- This test drive already Cloned the repo and has all the needed files.

- Create Lab topology using Containerlab
```html
  cd keng-td/ixia-c/lab1
  sudo containerlab deploy -t lab1-clab-topology.yml 
```

- Check running containers
```html
docker ps
```
- Lab1-A: Send undirectional traffic: Port-1 to Dut to Port-2
- Use otgen cli to execute the test with the updated MAC addresses and the IP addresses used to create the raw traffic flows.
```html
source lab1-undirectional.sh
``` 
- Verify results. You should have seen 2000 frames sent and 2000 recieved.
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
