# Lab #2 – KENG + CURL JSON + CONTAINER LAB + FRR DUT + BGP

## Description
This lab introduces the concept of Network Topology Emulation via the Container Lab software. This software is in charge of container orchestration (similar to Docker Compose) and also takes care of the underlying network connections (equivalent to creating virtual point-to-point Ethernet interfaces).
This lab uses CURL JSON  to control the KENG Commercial Edition (OTG Test Tool) which is utilized to send dynamic traffic through a FRR DUT. This lab consists of 1x Controller container, 2x keng Traffic Engine containers, 2x keng protocol engine and 1x FRR container.


## Prerequites 
None! All files and images are included.

## Start Lab2
- This test drive already Cloned the repo and has all the needed files.

- Create Lab topology using Containerlab
```html
  cd keng-td/keng/lab2
```
```html
  sudo containerlab deploy -t lab2-clab-topology.yml 
  ```

- Check running containers
```html
docker ps
```
### Lab2: Send undirectional traffic: Port-1 to Dut to Port-2
- Using CURL JSON to execute the test with the updated MAC addresses and the IP addresses we got from the dynamic traffic flows.
- Load the test configurations
```html
source lab2-test-apply-config.sh
``` 
- The output of "warning" is OK.
- Start BGP Protocol 
```html
source lab2-test-start-protocol.sh
``` 
- verify bgp neighbor established; you can exec to the DUT and check bgp 
- Start transmitting data 1000 PPS for 100K frame 
```html
source lab2-test-start-traffic.sh
```
- Check results;  hit cntl+c to exit
```html
source lab2-test-show-results.sh

```
- Cleanup Lab
```html
sudo containerlab destroy -t lab2-clab-topology.yml
``` 
- Verify no more running containers
```html
docker ps
```
