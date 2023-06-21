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
                if h < 9:
                    h+=1
                    continue
                h = 0
                while self.arr[h]:
                    h+=1
                    
            self.arr[h] = value
        self.arr[h] = value
        

    def __getitem__(self,key):
        h = self.get_hash(key)
        return self.arr[h][1]
        
    
    def __delitem__(self,key):
        h = self.get_hash(key)
        self.arr[h] = None
        
    
        
    

table = Hash_Table()
table["March 9"] = 11
table["March 9"] = 12

print(table.arr)

    



        