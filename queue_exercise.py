from collections import deque
import time
import threading

class Queue:
    
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
        
    def dequeue(self):
        if len(self.buffer) == 0:
            print("Queue is empty")
            return
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)
    
    def front(self):
        return(self.buffer[-1])

orders = Queue()
ordered = ["pizza","hamburger","gyros","apple pie"]

def place_order(order_names,queue):
    for order in order_names:
        print(f"Placing order for {order}")
        queue.enqueue(order)
        time.sleep(0.5)
        print("order placed")
        
        

def serve_order(queue: Queue):
    time.sleep(1)
    while True:
        print(f"Serving order: {queue.dequeue()}")
        time.sleep(0.5)
        if queue.is_empty():
            break

t1 = threading.Thread(target=place_order, args=(ordered,orders,))
t2 = threading.Thread(target=serve_order, args=(orders,))

t1.start()
time.sleep(1)
t2.start()

t1.join()
t2.join()



