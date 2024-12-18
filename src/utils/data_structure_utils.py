from src.data_structures.avl_tree import AVLTree
from src.data_structures.hash_table import HashTable
from src.data_structures.priority_queue import PriorityQueue
from src.data_structures.graph import Graph
from src.algorithms.search_algorithms import SearchAlgorithms
from src.algorithms.sort_algorithms import SortAlgorithms

class DataStructureManager:
    def __init__(self):
        self.customer_tree = AVLTree()
        self.account_hash_table = HashTable()
        self.transaction_queue = PriorityQueue()
        self.network_graph = Graph()

    def add_customer_to_tree(self, customer_id, customer):
        """
        Add customer to AVL Tree for efficient lookup
        """
        self.customer_tree.insert_key(customer_id, customer)

    def cache_account(self, account_number, account):
        """
        Cache account in hash table
        """
        self.account_hash_table.insert(account_number, account)

    def prioritize_transaction(self, transaction, priority):
        """
        Add transaction to priority queue
        """
        self.transaction_queue.push(transaction, priority)

    def map_customer_network(self, customer_id, related_customers):
        """
        Create a network graph of customer relationships
        """
        for related_customer in related_customers:
            self.network_graph.add_edge(customer_id, related_customer)

class AlgorithmUtility:
    @staticmethod
    def search_customers(customers, target_id):
        """
        Search customers using different algorithms
        """
        # Linear search
        linear_result = SearchAlgorithms.linear_search(
            [c.customer_id for c in customers], 
            target_id
        )

        # Binary search (requires sorted list)
        sorted_customers = SortAlgorithms.merge_sort(
            customers, 
            key=lambda x: x.customer_id
        )
        binary_result = SearchAlgorithms.binary_search(
            [c.customer_id for c in sorted_customers], 
            target_id
        )

        return {
            'linear_search': linear_result,
            'binary_search': binary_result
        }

    @staticmethod
    def analyze_transactions(transactions):
        """
        Analyze and sort transactions
        """
        # Sort transactions by amount
        sorted_by_amount = SortAlgorithms.quick_sort(
            transactions, 
            key=lambda x: x.amount
        )

        # Sort transactions by timestamp
        sorted_by_timestamp = SortAlgorithms.merge_sort(
            transactions, 
            key=lambda x: x.timestamp
        )

        return {
            'sorted_by_amount': sorted_by_amount,
            'sorted_by_timestamp': sorted_by_timestamp
        }