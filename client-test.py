import os, time
from gevent import Greenlet, sleep

l = []
t1 = time.time()
for i in xrange(0, 100000):  # also try a milion :)
   t = Greenlet(sleep, 30)
   t.start()
   l.append(t)

t2 = time.time()
print "%i coroutines created in %d seconds." % (len(l), t2-t1)

for t in l:
   t.join()

