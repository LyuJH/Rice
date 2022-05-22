#!/bin/bash

gateway_ip=$(grep gateway /etc/network/interfaces |awk '/gateway/ {print $2}')
echo "gateaway ip is" $gateway_ip
ping -c 50 $gateway_ip
