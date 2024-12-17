class AccountGraph:
    def __init__(self):
        self.graph = {}
    
    def add_account(self, account_id):
        """Add an account to the graph"""
        if account_id not in self.graph:
            self.graph[account_id] = set()
    
    def add_connection(self, account1, account2):
        """Add a connection between two accounts"""
        self.add_account(account1)
        self.add_account(account2)
        
        self.graph[account1].add(account2)
        self.graph[account2].add(account1)
    
    def get_connections(self, account_id):
        """Get all connections for a given account"""
        return self.graph.get(account_id, set())
    
    def is_connected(self, account1, account2):
        """Check if two accounts are connected"""
        return account1 in self.graph and account2 in self.graph[account1]
    
    def find_path(self, start, end, path=None):
        """Find a path between two accounts"""
        if path is None:
            path = []
        
        path = path + [start]
        
        if start == end:
            return path
        
        if start not in self.graph:
            return None
        
        for account in self.graph[start]:
            if account not in path:
                new_path = self.find_path(account, end, path)
                if new_path:
                    return new_path
        
        return None
    
    def __str__(self):
        """String representation of the account graph"""
        return str(self.graph)