#!/bin/bash -xe

export OTG_API="https://localhost:8443"

otgen run --insecure --metrics flow --interval 250ms -f otg-unidirectional.json --json --rxbgp 2x  | \
otgen transform --metrics flow --counters frames | \
otgen display --mode table
