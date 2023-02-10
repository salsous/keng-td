from time     import time
from datetime import datetime
from snappi   import snappi

def Traffic_Test():

    ## This script does following:
    ## - Send 2000 packets back and forth between the two ports at a rate of 100 packets per second.
    ## - Validate that total packets sent and received on both interfaces is as expected using port metrics.

    starttime = datetime.now()

    # Configure a new API instance where the location points to controller
    # Ixia-C:       location = "https://<tgen-ip>:<port>"
    # IxNetwork:    location = "https://<tgen-ip>:<port>", ext="ixnetwork"
    # TRex:         location =         "<tgen-ip>:<port>", ext="trex"

    print("")
    api = snappi.api(location="https://clab-Ixia-c-DUT-FRR-Ixia-c-Controller:8443", verify=False)
    print("%s Starting connection to controller                     ... " % datetime.now())

    # Create an empty configuration to be pushed to controller
    configuration = api.config()

    # Configure two ports where the location points to the port location:
    # Ixia-C:       port.location = "localhost:5555"
    # IxNetwork:    port.location = "<chassisip>;card;port"
    # TRex:         port.location = "localhost"

    port1, port2 = (
        configuration.ports
        .port(name="Port-1", location="clab-Ixia-c-DUT-FRR-Ixia-c-Traffic-Engine-1:5551")
        .port(name="Port-2", location="clab-Ixia-c-DUT-FRR-Ixia-c-Traffic-Engine-2:5552")
    )

    # Configure two traffic flows
    flow1, flow2 = (
        configuration.flows
        .flow(name="Flow #1 - Port 1 > Port 2")
        .flow(name="Flow #2 - Port 2 > Port 1")
    )

    # v2. (e) Send traffic with both flows in the same direction instead of sending bidirectional traffic.
    flow1.tx_rx.port.tx_name = port1.name
    flow1.tx_rx.port.rx_name = port2.name
    flow2.tx_rx.port.tx_name = port1.name
    flow2.tx_rx.port.rx_name = port2.name

    # v2. (c) Send traffic with a frame size of 512 bytes instead of 128 bytes in each direction.
    flow1.size.fixed = 512
    flow2.size.fixed = 512
    for f in configuration.flows:
        # v2. (b) Send traffic with a duration of 5 seconds instead of 20 seconds.
        f.duration.fixed_packets.packets = 1000
        # v2. (a) Send traffic with a rate of 200 fps instead of 100 fps.
        f.rate.pps = 200

    # v2. (d) Send traffic with ETH + IP + TCP packet structure instead of ETH + IP + UDP packet structure.
    flow1.packet.ethernet().ipv4().tcp()
    flow2.packet.ethernet().ipv4().tcp()
    eth1, ip1, tcp1 = flow1.packet[0], flow1.packet[1], flow1.packet[2]
    eth2, ip2, tcp2 = flow2.packet[0], flow2.packet[1], flow2.packet[2]

    # Configure source and destination MAC addresses
    eth1.src.value, eth1.dst.value = "00:AA:00:00:01:00", "00:AA:00:00:02:00"
    eth2.src.value, eth2.dst.value = "00:AA:00:00:03:00", "00:AA:00:00:04:00"

    # Configure source and destination IPv4 addresses
    ip1.src.value, ip1.dst.value = "192.0.2.1", "192.0.2.5"
    ip2.src.value, ip2.dst.value = "192.0.2.1", "192.0.2.5"

    # Configure UDP Ports Source as incrementing
    tcp1.src_port.increment.start = 5100
    tcp1.src_port.increment.step  = 2
    tcp1.src_port.increment.count = 10
    tcp2.src_port.increment.start = 5200
    tcp2.src_port.increment.step  = 4
    tcp2.src_port.increment.count = 10

    # Configure UDP Ports Destination as value list
    tcp1.dst_port.values = [6100, 6125, 6150, 6170, 6190]
    tcp2.dst_port.values = [6200, 6222, 6244, 6266, 6288]

    print("%s Starting configuration apply                          ... " % datetime.now())
    api.set_config(configuration)

    print("%s Starting transmit on all flows                        ... " % datetime.now())
    ts = api.transmit_state()
    ts.state = ts.START
    api.set_transmit_state(ts)

    print("%s Starting statistics verification on all ports         ... " % datetime.now())
    print("====================================================================================")
    print("\t\t\t\t\t\tExpected\tTx\t\tRx")
    assert wait_for(lambda: verify_statistics(api, configuration)), "%s Test is FAILED in %s" % (datetime.now(), datetime.now() - starttime)
    print("====================================================================================")
    print("%s Test is PASSED in %s                                      " % (datetime.now(), datetime.now() - starttime))
    print("")


def verify_statistics(api, configuration):

    # Create a port statistics request and filter based on port names
    statistics = api.metrics_request()
    statistics.port.port_names = [p.name for p in configuration.ports]

    # Create a filter to include only sent and received packet statistics
    statistics.port.column_names = [statistics.port.FRAMES_TX, statistics.port.FRAMES_RX]

    # Collect port statistics
    results = api.get_metrics(statistics)

    # Calculate total frames sent and received across all ports
    total_frames_tx = sum([m.frames_tx for m in results.port_metrics])
    total_frames_rx = sum([m.frames_rx for m in results.port_metrics])
    total_expected  = sum([f.duration.fixed_packets.packets for f in configuration.flows])

    print("%s TOTAL  \t\t%d\t\t%d\t\t%d" % (datetime.now(), total_expected, total_frames_tx, total_frames_rx))

    return total_expected == total_frames_tx and total_frames_rx >= total_expected


def wait_for(func, timeout=30, interval=0.25):

    # Keeps calling the `func` until it returns true or `timeout` occurs every `interval` seconds.

    import time

    start = time.time()

    while time.time() - start <= timeout:
        if func():
            return True
        time.sleep(interval)

    return False


if __name__ == "__main__":
    Traffic_Test()
