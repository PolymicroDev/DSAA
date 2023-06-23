class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self,data):
        if self.head == None:
            self.head = Node(data, self.head, None)

        else:
            node = Node(data,self.head,None)
            self.head.prev = node
            self.head = node
    
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
    
    def get_last_node(self):
        itr = self.head

        while itr.next:
            itr = itr.next
        return itr

    def print_backwards(self):
        if self.head is None:
            print("Linked list is empty")
            return
        llst = ''
        itr = self.get_last_node()
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
            self.head.prev = None
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                itr.next.prev = itr
                break

            itr = itr.next
            count +=1

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        found = False
        while itr:
            if itr.data == data_after:
                found = True
                break
            itr = itr.next
        if found == False:
            raise Exception("Data not found")
        itr.next = Node(data_to_insert,itr.next,itr)
        
    def remove_by_value(self,data):
        index = 0
        itr = self.head
        while itr:
            if itr.data == data:
                self.remove_at(index)
                return
            itr = itr.next
            index +=1
        raise Exception("Data not found")


ll = LinkedList()
ll.insert_values(["Mango","Ananas","Apple","Orange"])
print("Backwards:")
ll.print_backwards()
print("Forward:")
ll.print_forward()
ll.remove_at(2)
ll.print_forward()
ll.insert_at_end("Apple")
ll.print_forward()
ll.insert_after_value("Mango","Banana")
ll.print_forward()