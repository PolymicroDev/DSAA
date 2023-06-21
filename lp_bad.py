class Hash_Table:
    def __init__(self):
        self.MAX = 10
        self.arr =  [None for i in range(self.MAX)]
    
    def get_hash(self,key):
        h = 0
        for i in key:
            h += ord(i)
        return h%self.MAX
    
    def __setitem__(self,key,value):
        h = self.get_hash(key)
        if self.arr[h]:
            if self.arr[h+1]:
                i=0
                while self.arr[i]:
                    i+=1
                self.arr[i] = value
            else:
                self.arr[h+1] = value
        else:
            self.arr[h] = value


    def __getitem__(self,key):
        h = self.get_hash(key)
        
        
    
    def __delitem__(self,key):
        h = self.get_hash(key)
    
        
    
    

table = Hash_Table()
table["March 2"] = 133
print(table.arr)


    



        