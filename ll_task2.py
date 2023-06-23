class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self,data):
        self.head = Node(data, self.head, None)
    
    def print_forward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data)
            itr = itr.next

            if itr is not None:
                llstr+= str("<-->")
        print(llstr)
    
    def print_backwards(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head

        while itr.next:
            itr = itr.next
        llst = ''

        while itr:
            llst+= str(itr.data)
            itr = itr.prev

            if itr is not None:
                llst+= str("<-->")
            
        print(llst)

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None,None)
            return

        itr = self.head
        while itr.next:
            
            itr = itr.next
        
        itr.next = Node(data,None,itr)
    
    def insert_values(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)
    
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count
    
    def remove_at(self,index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count +=1


ll = LinkedList()
ll.insert_values(["Mango","Ananas","Apple","Orange"])
print("Backwards:")
ll.print_backwards()
print("Forward:")
ll.print_forward()