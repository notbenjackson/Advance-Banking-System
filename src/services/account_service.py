from typing import List, Optional
from src.core.account import Account
from src.data_structures.avl_tree import AVLTree
from src.data_structures.hash_table import HashTable
from src.algorithms.search_algorithms import SearchAlgorithms
from src.algorithms.sort_algorithms import SortAlgorithms

class AccountService:
    def __init__(self):
        # Use AVL Tree for efficient account storage and retrieval
        self.account_tree = AVLTree()
        
        # Use Hash Table for fast account lookups
        self.account_cache = HashTable()

    def create_account(
        self, 
        customer_id: str, 
        account_type: str = 'Savings', 
        initial_balance: float = 0.0
    ) -> Optional[Account]:
        """
        Create a new bank account using AVL Tree and Hash Table
        """
        # Create account
        new_account = Account(
            customer_id=customer_id,
            account_type=account_type,
            balance=initial_balance
        )

        # Insert into AVL Tree (key: account number)
        self.account_tree.insert_key(new_account.account_number, new_account)
        
        # Cache in Hash Table
        self.account_cache.insert(new_account.account_number, new_account)

        return new_account

    def find_account(self, account_number: str) -> Optional[Account]:
        """
        Find account using multiple search algorithms
        """
        # First, check hash table for O(1) lookup
        if self.account_cache.contains(account_number):
            return self.account_cache.get(account_number)

        # Fallback to AVL Tree search
        avl_result = self.account_tree.find(account_number)
        if avl_result:
            return avl_result.value

        return None

    def get_customer_accounts(self, customer_id: str) -> List[Account]:
        """
        Retrieve and sort customer accounts
        """
        # Collect all accounts for the customer
        customer_accounts = []
        
        # Traverse AVL Tree to find accounts
        def collect_accounts(node):
            if not node:
                return
            
            if node.value.customer_id == customer_id:
                customer_accounts.append(node.value)
            
            collect_accounts(node.left)
            collect_accounts(node.right)

        collect_accounts(self.account_tree.root)

        # Sort accounts using merge sort
        return SortAlgorithms.merge_sort(
            customer_accounts, 
            key=lambda x: x.balance
        )

    def search_accounts(
        self, 
        search_term: str, 
        search_type: str = 'account_number'
    ) -> List[Account]:
        """
        Advanced account search using multiple algorithms
        """
        all_accounts = []
        
        # Collect all accounts from AVL Tree
        def collect_all_accounts(node):
            if not node:
                return
            
            all_accounts.append(node.value)
            collect_all_accounts(node.left)
            collect_all_accounts(node.right)

        collect_all_accounts(self.account_tree.root)

        # Sort accounts for binary search
        sorted_accounts = SortAlgorithms.merge_sort(
            all_accounts, 
            key=lambda x: getattr(x, search_type)
        )

        # Perform different searches based on type
        if search_type == 'account_number':
            # Binary search for account number
            binary_result = SearchAlgorithms.binary_search(
                [a.account_number for a in sorted_accounts], 
                search_term
            )
            
            # Fallback to linear search
            linear_result = SearchAlgorithms.linear_search(
                [a.account_number for a in all_accounts], 
                search_term
            )

            # Combine results
            results = []
            if binary_result is not None:
                results.append(sorted_accounts[binary_result])
            if linear_result is not None:
                results.append(all_accounts[linear_result])

            return results

        # Fallback to linear search for other attributes
        return [
            account for account in all_accounts 
            if search_term.lower() in str(getattr(account, search_type)).lower()
        ]