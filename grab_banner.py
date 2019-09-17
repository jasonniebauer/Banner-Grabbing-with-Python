#! /usr/bin/env python

import socket

socket.setdefaulttimeout(2)
s = socket.socket()
s.connect(('www.google.com', 80))
s.send(b'GET /\n\n')
banner = s.recv(1024)
print(banner)
