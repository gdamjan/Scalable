#! /usr/bin/env python
import asyncore, socket

class Client(asyncore.dispatcher_with_send):
    def __init__(self, host, port, message, n):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, port))
        self.out_buffer = message
        self.N = n

    def handle_close(self):
        self.N = self.N - 1
        self.close()

    def handle_read(self):
        self.N = self.N - 1
        buf = self.recv(1024)
        print 'Received: %s' % buf
        if self.N == 0:
            raise "STOP"
#        self.close()  # so I'm not closing it

def main(n):
    host, port = 'localhost', 9901
    print "Opening %d connections to %s:%d" % (n, host, port)
    for i in xrange(n):
        Client(host, port, 'Hello, world!', n)
    asyncore.loop()

import sys
try:
    main(int(sys.argv[1]))
except KeyboardInterrupt:
    sys.exit(0)
