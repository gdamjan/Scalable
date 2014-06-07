from gevent.pywsgi import WSGIServer
import gevent


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    for x in range(300):
        gevent.sleep(0.1)
        #for i in xrange(1,100000000): pass # block cpu
        yield "%d\n" % x

if __name__ == "__main__":
    print 'Serving on 8088...'
    WSGIServer(('', 8088), application).serve_forever()


