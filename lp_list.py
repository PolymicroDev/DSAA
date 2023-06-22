class Hash_Table:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]
    
    def get_hash(self,key):
        h = 0
        for i in key:
            h += ord(i)
        return h%self.MAX
    
    def __setitem__(self,key,value):
        h = self.get_hash(key)
        if self.arr[h]:
            while self.arr[h]:
                if h < len(self.arr)-1:
                    h+=1
                else:
                    h = 0
            if not self.arr[h]:
                self.arr[h] = (key,value)
                return
            raise Exception("Out of space, unable to add key")
        self.arr[h] = (key,value)
        

    def __getitem__(self,key):
        h = self.get_hash(key)
        if self.arr[h]:
            if self.arr[h][0] == key:
                return self.arr[h][1]
            
            h = 0
            while self.arr[h][0] != key:
                if h < len(self.arr)-1:
                    h+=1

            if self.arr[h][0] == key:
                return self.arr[h][1]
            raise Exception("Didn't find key.")
        raise Exception("No key")
        
        
        
    
    def __delitem__(self,key):
        h = self.get_hash(key)
        if self.arr[h]:
            if self.arr[h][0] == key:
                self.arr[h] = None
                return
            
            h = 0
            while self.arr[h][0] != key:
                if h < len(self.arr)-1:
                    h+=1

            if self.arr[h][0] == key:
                self.arr[h] = None
                return
            raise Exception("Didn't find key.")
        raise Exception("No key")
        
        
    
        
    

table = Hash_Table()
table["March 9"] = 11
table["March 10"] = 14
table["9 March"] = 13
table["March 11"] = 112
table["11 March"] = 129
table["March 22"] = 122
table["March 23"] = 111
table["March 25"] = 115
table["March 27"] = 110



print(table.arr)
print(table["9 March"])
del table["9 March"]
print(table.arr)

    



        