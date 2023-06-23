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
                elif h == len(self.arr)-1 and self.arr[h]:
                    break
                else:
                    h = 0
                
            if self.arr[h] is None:
                self.arr[h] = (key,value)
                return
            raise Exception("Out of space, unable to add key")
        self.arr[h] = (key,value)
        

    def __getitem__(self,key):
        h = self.get_hash(key)
        if self.arr[h]:
            if self.arr[h][0] == key:
                return self.arr[h][1]
            
            
            while self.arr[h][0] != key and self.arr[h][0]:
                if h < len(self.arr)-1:
                    h+=1
                elif h == len(self.arr)-1 and self.arr[h][0]:
                    break
                else:
                    h = 0
        
            if self.arr[h][0] == key and self.arr[h][0]:
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
table["March 12"] = 11
table["March 13"] = 15
table["March 28"] = 19
table["March 229"] = 122
table["March 918"] = 12
table["March 888"] = 134
table["March 1234"] = 120
table["March 1981"] = 12
table["March 2"] = 987
table["March 6"] = 919

 

print(table.get_hash("March 1234"))
print(table.arr)

print(table["March 2"])

    



        