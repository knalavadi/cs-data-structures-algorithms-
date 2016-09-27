'''Hashmap practice'''


'''
        difference ways to hash keys: 

        index = len(key)-1
        index = sum(ASCII value for each letter in key) %5

            for char in key:
                hash += ord(char)
            hash %= 5 

'''    

class HashMap:
    def __init__(self):
        #size of array (sample size)
        self.size = 6 
        #array to store data in, initalize every cell equal to None
        self.map = [None] * self.size


    def get_hash(self, key):
        '''calculates index for key'''
        hash = 0 
        for char in str(key):
            hash += ord(char)
        return hash % self.size    

    def add(self, key, value):
        '''add key and values'''
        key_hash = self._get_hash(key) #gets key 
        key_value = [key, value] #constructing key and value list, (what we want to put in cell)

        if self.key[key_hash] is None: #checking if cell is empty
            self.map[key_hash] = list([key_value]) #adding key value pair
            return True 

        else:
            for pair in self.map[key_hash]: # if not empty
                if pair[0] == key #if key is existing update value 
                    pair[1] == value 
                    return True 
            self.map[key_hash].append(key_value) #if key is not existing append key value pair ot the list 
            return True             
    
    def get(self, key):
        '''gets value for key'''
        key_hash = self._get_hash(key) 
        if self.map[key_hash] is not None: #locates cell, if not None:
            for pair in self.map[key_hash]: # iterates through pairs in that cell 
                if pair[0] == key: #value that matches that key 
                    return pair[1] #returns value 
        return None 
        
    def delete(self, key):
        '''deletes key value pair'''
        key_hash = self._get_hash(key)

        if self.map[key_hash] is None: #checks if cell is none 
            return False

        for i in range (0, len(self.map[key_hash])): #iterates through items in cells 
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i) #removes item 
                return True 
            















