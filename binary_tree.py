class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self,data):
        if data == self.data:
            return
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
    
    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()
        
        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()
        
        return elements
    
    def pre_order_traversal(self):
        elements = []

        elements.append(self.data)

        if self.left:
            elements += self.left.pre_order_traversal()
        
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()
        
        if self.right:
            elements += self.right.post_order_traversal()
        
        elements.append(self.data)

        return elements
    
    def min(self):
        if not self.data:
            raise Exception("Binary Tree is empty")
        
        itr = self
        while itr.left:
            itr = itr.left
        
        return itr.data
        
    def max(self):
        if not self.data:
            raise Exception("Binary Tree is empty")
        
        itr = self
        while itr.right:
            itr = itr.right
        
        return itr.data
        
        
    def sum_values(self):
        elements = self.in_order_traversal()
        sum = 0

        for i in elements:
            sum += i
        return sum
    
    def search(self,val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
            
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)

        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)

        else:
            if self.left == None and self.right == None:
                return None
            if self.left == None:
                return self.right
            if self.right == None:
                return self.left
            
            min_val = self.right.min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self

    def delete_max(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete_max(val)

        elif val > self.data:
            if self.right:
                self.right = self.right.delete_max(val)

        else:
            if self.left == None and self.right == None:
                return None
            if self.left == None:
                return self.right
            if self.right == None:
                return self.left

            max_val = self.left.max()
            self.data = max_val
            self.left = self.left.delete_max(max_val)

        return self

            

    
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    
    return root

if __name__ == '__main__':
    numbers = [17,4,1,20,9,23,18,34]
    numbers_tree = build_tree(numbers)
    numbers_tree.delete_max(20)
    print("After deleting 20 ", numbers_tree.in_order_traversal())  # this should print [1, 4, 9, 17, 18, 23, 34]
