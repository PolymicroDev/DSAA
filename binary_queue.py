from collections import deque

class Queue:
    
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return
        return self.buffer.pop()
    
    def front(self):
        if self.is_empty():
            print("Queue is empty")
            return
        return self.buffer[-1]
    def items(self):
        list = []
        for i in self.buffer:
            list.append(i)

        return list
    def size(self):
        return len(self.buffer)
    
def produce_binary_numbers(n):
    numbers_queue = Queue()
    numbers_queue.enqueue("1")
    for i in range(n):
        front = numbers_queue.front()
        print("   ", front)
        numbers_queue.enqueue(front + "0")
        numbers_queue.enqueue(front + "1")

        numbers_queue.dequeue()
    
produce_binary_numbers(10)

    


    

    
