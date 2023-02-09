# Lab #2 – KENG + SNAPPI + CONTAINER LAB + FRR DUT + BGP

## Description
This lab introduces the concept of Network Topology Emulation via the Container Lab software. This software is in charge of container orchestration (similar to Docker Compose) and also takes care of the underlying network connections (equivalent to creating virtual point-to-point Ethernet interfaces).
This lab uses SNAPPI  to control the KENG Commercial Edition (OTG Test Tool) which is utilized to send raw traffic through a FRR DUT. This lab consists of 1x Controller container, 2x keng Traffic Engine containers, 2x keng protocol engine and 1x FRR container.


## Prerequites 
Git clone repo to get all needed files below
- 1- lab2-DUT-FRR-config1.
- 2-lab2-DUT-FRR-daemons.
- 3-lab2-clab-topology.yml.
- 4- lab2-test-script.py.

## Start Lab1
- Clone the repo
