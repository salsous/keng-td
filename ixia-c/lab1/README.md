
# Lab #1 – IXIA-C + OTGEN CLI + CONTAINER LAB + FRR DUT

## Description
This lab introduces the concept of Network Topology Emulation via the Container Lab software. This software is in charge of container orchestration (similar to Docker Compose) and also takes care of the underlying network connections (equivalent to creating virtual point-to-point Ethernet interfaces).
This lab uses OTGEN CLI (OTG API Client) to control the free Ixia-c Community Edition (OTG Test Tool) which is utilized to send raw traffic through a FRR DUT. This lab consists of 1x Ixia-c Controller container, 2x Ixia-c Traffic Engine containers, and 1x FRR container.


## Prerequites 
None! All files and images are included.

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
### Lab1-A: Send undirectional traffic: Port-1 to Dut to Port-2
- Use otgen cli to execute the test with the updated MAC addresses and the IP addresses used to create the raw traffic flows.
```html
source lab1-test-unidirectional.sh
``` 
- Verify results; 1000 frames sent and 1000 recieved.
- 
![lab1-uni-dir](https://user-images.githubusercontent.com/13612422/219531107-089e2a71-ce54-4a46-b267-9641a2a51c66.png)
-
### Lab1-B: Send bidirectional traffic: Port-1 <-> Port-2
- Use otgen cli to execute the test with the updated MAC addresses and the IP addresses used to create the raw traffic flows.
```html
source lab1-test-bidirectional.sh
``` 
- Verify results;  1000 frames sent and 1000 recieved in both directions
-
![lab1-bi-dir](https://user-images.githubusercontent.com/13612422/219531506-30442ec3-cab2-47eb-b7b7-fcb1f881ae19.png)
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
