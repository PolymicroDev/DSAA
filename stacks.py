from collections import deque
s = []
s.append("https://cnn.com/")
s.append("https://cnn.com/world")
s.append("https://cnn.com/india")
s.append("https://cnn.com/china")

stack = deque()
stack.append("https://cnn.com/")
stack.append("https://cnn.com/world")
stack.append("https://cnn.com/india")
stack.append("https://cnn.com/china")

print(stack)
print(stack.pop())
print(stack)

class Stack:
    def __init__(self):
        self.container = deque()
        
    def push(self,val):
        self.container.append(val)
    
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)

    def reverse_string(self,string: str):
        reversed_string = ''
        stack_string = Stack()
        
        for i in string:
            stack_string.push(i)

        while not stack_string.is_empty():
            reversed_string += stack_string.pop()

        return reversed_string

    def is_balanced(self):
        pass

s1 = Stack()
print(s1.reverse_string("Covid 19"))

