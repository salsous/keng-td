
# Lab #1A – IXIA-C + OTGEN CLI + CONTAINER LAB + FRR DUT
Git clone repo to get all needed files
1- lab1-DUT-FRR-config1.
2-lab1-DUT-FRR-daemons.
3-lab1-clab-topology.yml.
4- lab1-test-script.py.


cd ./ixia-c/lab1
cat lab1-clab-topology.yml

sudo containerlab deploy -t lab1-clab-topology.yml

Check running containers
docker ps
