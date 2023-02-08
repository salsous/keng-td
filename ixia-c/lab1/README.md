
# Lab #1A – IXIA-C + OTGEN CLI + CONTAINER LAB + FRR DUT

## Description
This lab introduces the concept of Network Topology Emulation via the Container Lab software. This software is in charge of container orchestration (similar to Docker Compose) and also takes care of the underlying network connections (equivalent to creating virtual point-to-point Ethernet interfaces).
This lab uses OTGEN CLI (OTG API Client) to control the free Ixia-c Community Edition (OTG Test Tool) which is utilized to send raw traffic through a FRR DUT. This lab consists of 1x Ixia-c Controller container, 2x Ixia-c Traffic Engine containers, and 1x FRR container.



Git clone repo to get all needed files
- 1- lab1-DUT-FRR-config1.
- 2-lab1-DUT-FRR-daemons.
- 3-lab1-clab-topology.yml.
- 4- lab1-test-script.py.


- cd ./ixia-c/lab1
-- cat lab1-clab-topology.yml

-- sudo containerlab deploy -t lab1-clab-topology.yml

- Check running containers
-- docker ps
