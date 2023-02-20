# Lab #2 – KENG + SNAPPI + CONTAINER LAB + FRR DUT + BGP

## Description
This lab introduces the concept of Network Topology Emulation via the Container Lab software. This software is in charge of container orchestration (similar to Docker Compose) and also takes care of the underlying network connections (equivalent to creating virtual point-to-point Ethernet interfaces).
This lab uses SNAPPI  to control the KENG Commercial Edition (OTG Test Tool) which is utilized to send raw traffic through a FRR DUT. This lab consists of 1x Controller container, 2x keng Traffic Engine containers, 2x keng protocol engine and 1x FRR container.


## Prerequites 
None! All files and images are included.

## Start Lab2
- This test drive already Cloned the repo and has all the needed files.

- Create Lab topology using Containerlab
```html
  cd keng-td/ixia-c/lab2
```
```html
  sudo containerlab deploy -t lab2-clab-topology.yml 
  ```

- Check running containers
```html
docker ps
```
### Lab2: Send undirectional traffic: Port-1 to Dut to Port-2
- Using SNAPPI Script to execute the test with the updated MAC addresses and the IP addresses we got from the dynamic traffic flows.
```html
source lab2-test-unidirectional.sh
``` 
- Verify results; 1000 frames sent and 1000 recieved.
- 
![lab2-uni-dir](https://user-images.githubusercontent.com/13612422/219709266-2f893236-0503-44d3-bf8b-4d8c8271c25f.png)
-
- Cleanup Lab
```html
sudo containerlab destroy -t lab2-clab-topology.yml
``` 
- Verify no more running containers
```html
docker ps
```
