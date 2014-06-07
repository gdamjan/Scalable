#! /usr/bin/env python

import gevent
from gevent import socket

def make_connection(host, port, message, n):
    sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sc.connect((host, port))
    sc.send(message)
    buf = sc.recv(1024)
    if buf == message:
        return "Sucess %d" % n
    else:
        return "Error %d" % n

def main(n):
    host, port = 'localhost', 9901
    print "Opening %d connections to %s:%d" % (n, host, port)
    l = []
    for i in xrange(n):
        t = gevent.spawn(make_connection, host, port, 'Hello, world!', i)
        l.append(t)
    for t in l:
        print t.get()
    gevent.sleep(1000)

import sys
try:
    main(int(sys.argv[1]))
except KeyboardInterrupt:
    sys.exit(0)
