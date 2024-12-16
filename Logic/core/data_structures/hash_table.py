class BankingHashTable:
    def __init__(self, size=100):
        """
        Initialize the hash table with a given size.
        
        Args:
            size (int): The size of the hash table. Default is 100.
        """
        self.size = size
        # Create a list of 'size' elements, each initialized to None
        self.table = [None] * size
    
    def _hash_function(self, key):
        """
        Simple hash function to convert a key to an index.
        
        Args:
            key (str): The key to be hashed (typically a username or account number)
        
        Returns:
            int: The index in the hash table
        """
        # Sum the ASCII values of characters and use modulo to fit within table size
        return sum(ord(char) for char in str(key)) % self.size
    
    def insert(self, key, value):
        """
        Insert a key-value pair into the hash table.
        
        Args:
            key (str): The key for the entry
            value (dict): The value to be stored (typically user account information)
        """
        # Calculate the index using hash function
        index = self._hash_function(key)
        
        # Handle collision using simple linear probing
        while self.table[index] is not None:
            # If the key already exists, update the value
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            
            # Move to next index (wrap around if needed)
            index = (index + 1) % self.size
        
        # Insert the new key-value pair
        self.table[index] = (key, value)
    
    def get(self, key):
        """
        Retrieve a value by its key.
        
        Args:
            key (str): The key to search for
        
        Returns:
            The value associated with the key, or None if not found
        """
        # Calculate the initial index
        index = self._hash_function(key)
        
        # Search for the key, handling potential collisions
        original_index = index
        while self.table[index] is not None:
            # Check if the current entry matches the key
            if self.table[index][0] == key:
                return self.table[index][1]
            
            # Move to next index
            index = (index + 1) % self.size
            
            # Stop if we've checked the entire table
            if index == original_index:
                break
        
        # Key not found
        return None
    
    def remove(self, key):
        """
        Remove a key-value pair from the hash table.
        
        Args:
            key (str): The key to remove
        
        Returns:
            bool: True if removed, False if not found
        """
        # Calculate the initial index
        index = self._hash_function(key)
        
        # Search for the key, handling potential collisions
        original_index = index
        while self.table[index] is not None:
            # Check if the current entry matches the key
            if self.table[index][0] == key:
                # Remove the entry
                self.table[index] = None
                return True
            
            # Move to next index
            index = (index + 1) % self.size
            
            # Stop if we've checked the entire table
            if index == original_index:
                break
        
        # Key not found
        return False

# Example usage
def main():
    # Create a hash table for bank accounts
    account_database = BankingHashTable()
    
    # Insert some sample account information
    account_database.insert("john_doe", {
        "account_number": "1234567890",
        "balance": 5000.00,
        "email": "john.doe@example.com"
    })
    
    account_database.insert("jane_smith", {
        "account_number": "0987654321",
        "balance": 7500.50,
        "email": "jane.smith@example.com"
    })
    
    # Retrieve account information
    john_account = account_database.get("john_doe")
    print("John's Account:", john_account)
    
    # Update an account
    account_database.insert("john_doe", {
        "account_number": "1234567890",
        "balance": 5500.00,
        "email": "john.doe@example.com"
    })
    
    # Remove an account
    account_database.remove("jane_smith")
    
    # Try to retrieve a removed account
    jane_account = account_database.get("jane_smith")
    print("Jane's Account:", jane_account)  # Should print None

if __name__ == "__main__":
    main()