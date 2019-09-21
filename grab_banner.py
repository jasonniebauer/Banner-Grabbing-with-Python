#! /usr/bin/env python

import socket

socket.setdefaulttimeout(2)
s = socket.socket()

target_ip = input('Enter IP address: ')
target_port = int(input('Enter port: '))

try:
    # Connect to the target IP address
    # s.connect(('www.google.com', 80))
    s.connect((target_ip, target_port))
    s.send(b'GET /\n\n')
    # Return the service being run on the target server
    banner = s.recv(1024)
    print(banner)
    print(type(banner))
except:
    print('Unable to connect to %s:%s' % (target_ip, target_port))
