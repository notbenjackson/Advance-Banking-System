class HashTable:
    def __init__(self, size=100):
        """
        Initialize the hash table with a given size.
        
        Args:
            size (int): The size of the hash table's internal list. Defaults to 100.
        """
        # Use a list of lists to handle collision via chaining
        self.size = size
        self.table = [[] for _ in range(self.size)]
    
    def _hash_function(self, key):
        """
        Generate a hash value for the given key.
        
        Args:
            key: The key to be hashed (can be string, integer, etc.)
        
        Returns:
            int: A hash index within the table's size
        """
        # Use built-in hash function and ensure it's within table size
        return hash(key) % self.size
    
    def insert(self, key, value):
        """
        Insert a key-value pair into the hash table.
        
        Args:
            key: The key to insert
            value: The value associated with the key
        """
        # Calculate the hash index
        index = self._hash_function(key)
        
        # Check if key already exists
        for item in self.table[index]:
            if item[0] == key:
                # Update existing key's value
                item[1] = value
                return
        
        # If key doesn't exist, append new key-value pair
        self.table[index].append([key, value])
    
    def get(self, key):
        """
        Retrieve the value associated with a given key.
        
        Args:
            key: The key to look up
        
        Returns:
            The value associated with the key, or None if key not found
        
        Raises:
            KeyError: If the key is not found in the hash table
        """
        # Calculate the hash index
        index = self._hash_function(key)
        
        # Search for the key in the bucket
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        
        # Key not found
        raise KeyError(f"Key '{key}' not found in hash table")
    
    def remove(self, key):
        """
        Remove a key-value pair from the hash table.
        
        Args:
            key: The key to remove
        
        Raises:
            KeyError: If the key is not found in the hash table
        """
        # Calculate the hash index
        index = self._hash_function(key)
        
        # Iterate through items in the bucket
        for i, item in enumerate(self.table[index]):
            if item[0] == key:
                # Remove the item if key is found
                del self.table[index][i]
                return
        
        # Key not found
        raise KeyError(f"Key '{key}' not found in hash table")
    
    def __str__(self):
        """
        Provide a string representation of the hash table.
        
        Returns:
            str: A string showing the contents of the hash table
        """
        output = []
        for i, bucket in enumerate(self.table):
            if bucket:
                output.append(f"Bucket {i}: {bucket}")
        return "\n".join(output) if output else "Empty Hash Table"

# Example usage
def main():
    # Create a hash table
    ht = HashTable(size=10)
    
    # Insert some key-value pairs
    ht.insert("name", "Alice")
    ht.insert("age", 30)
    ht.insert("city", "New York")
    
    # Print the hash table
    print("Hash Table Contents:")
    print(ht)
    
    # Retrieve values
    print("\nRetrieving values:")
    print("Name:", ht.get("name"))
    print("Age:", ht.get("age"))
    
    # Update a value
    ht.insert("age", 31)
    print("\nAfter updating age:")
    print("New Age:", ht.get("age"))
    
    # Remove a key
    ht.remove("city")
    print("\nAfter removing city:")
    print(ht)
    
    # Demonstrate error handling
    try:
        ht.get("city")
    except KeyError as e:
        print("\nError (as expected):", e)

if __name__ == "__main__":
    main()