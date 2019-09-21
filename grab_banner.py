#! /usr/bin/env python

import socket

socket.setdefaulttimeout(2)
s = socket.socket()

target_ip = input('Enter address: ')
target_port = int(input('Enter port: '))

try:
    # Connect to the target IP address
    # i.e. ('www.google.com', 80)
    s.connect((target_ip, target_port))
    s.send(b'GET /\n\n')
    # Return the service being run on the target server
    banner = s.recv(1024)
    # Decode response from bytes to string
    banner = banner.decode('utf-8')
    print(banner)
except:
    print('Unable to connect to %s:%s' % (target_ip, target_port))
