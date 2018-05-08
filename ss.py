from threading import Thread
import threading
def threaded(f, daemon=False):
    import Queue

    def wrapped_f(q, *args, **kwargs):
        ret = f(*args, **kwargs)
        q.put(ret)

    def wrap(*args, **kwargs):

        q = Queue.Queue()

        t = threading.Thread(target=wrapped_f, args=(q,)+args, kwargs=kwargs)
        t.daemon = daemon
        t.start()
        t.result_queue = q        
        return t

    return wrap

@threaded
def long_task(x):
    import time
    x = x + 5
    time.sleep(5)
    return x

# does not block, returns Thread object
y = long_task(10)
print y

# this blocks, waiting for the result
result = y.result_queue.get()
print result
