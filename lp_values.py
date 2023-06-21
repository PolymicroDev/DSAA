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
            while self.arr[h]:
                if h < 9:
                    h+=1
                    continue
                h = 0
                while self.arr[h]:
                    h+=1
                    
            self.arr[h] = (key,value)
        self.arr[h] = (key,value)


    def __getitem__(self,key):
        h = self.get_hash(key)
        
        
    
    def __delitem__(self,key):
        h = self.get_hash(key)
    
        
    
    

table = Hash_Table()
table["March 23"] = 112
table["March 10"] = 111
print(table.arr)


    



        