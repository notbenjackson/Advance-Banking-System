class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(self.size)]
    
    def _hash_function(self, key):
        """Simple hash function to convert key to index"""
        return hash(key) % self.size
    
    def insert(self, key, value):
        """Insert a key-value pair into the hash table"""
        index = self._hash_function(key)
        
        # Check if key already exists
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                return
        
        # If key doesn't exist, append new key-value pair
        self.table[index].append([key, value])
    
    def get(self, key):
        """Retrieve value for a given key"""
        index = self._hash_function(key)
        
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        
        raise KeyError(key)
    
    def delete(self, key):
        """Delete a key-value pair from the hash table"""
        index = self._hash_function(key)
        
        for i, item in enumerate(self.table[index]):
            if item[0] == key:
                del self.table[index][i]
                return
        
        raise KeyError(key)
    
    def __str__(self):
        """String representation of the hash table"""
        return str({k: v for bucket in self.table for k, v in bucket})