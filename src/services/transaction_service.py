from typing import List, Optional
from src.core.transaction import Transaction
from src.data_structures.priority_queue import PriorityQueue
from src.data_structures.graph import Graph
from src.algorithms.sort_algorithms import SortAlgorithms

class TransactionService:
    def __init__(self):
        # Priority Queue for managing transactions
        self.transaction_queue = PriorityQueue()
        
        # Graph to track transaction networks
        self.transaction_graph = Graph()

    def process_transaction(
        self, 
        from_account: str, 
        to_account: str, 
        amount: float
    ) -> Optional[Transaction]:
        """
        Process transaction using Priority Queue and Graph
        """
        # Create transaction
        transaction = Transaction.create_transaction(
            from_account, to_account, amount
        )

        # Calculate transaction priority
        priority = self._calculate_transaction_priority(transaction)

        # Add to priority queue
        self.transaction_queue.push(transaction, priority)

        # Add to transaction graph
        self.transaction_graph.add_edge(from_account, to_account, amount)

        return transaction

    def _calculate_transaction_priority(self, transaction: Transaction) -> float:
        """
        Calculate transaction priority based on amount and type
        """
        base_priority = transaction.amount
        
        # Add priority based on transaction type
        if transaction.transaction_type == 'INTERNATIONAL':
            base_priority *= 1.5
        
        return base_priority

    def get_account_transactions(
        self, 
        account_number: str, 
        limit: int = 10
    ) -> List[Transaction]:
        """
        Retrieve and analyze account transactions
        """
        # Collect transactions from graph
        transactions = []
        
        # Find all transactions related to the account
        for vertex in self.transaction_graph.vertices:
            if vertex == account_number:
                for neighbor, weight in self.transaction_graph.get_neighbors(vertex):
                    # Create a mock transaction for demonstration
                    transaction = Transaction.create_transaction(
                        vertex, neighbor, weight
                    )
                    transactions.append(transaction)

        # Sort transactions using multiple sorting algorithms
        sorted_by_amount = SortAlgorithms.quick_sort(
            transactions, 
            key=lambda x: x.amount
        )

        sorted_by_timestamp = SortAlgorithms.merge_sort(
            transactions, 
            key=lambda x: x.timestamp
        )

        return sorted_by_amount[:limit]

    def analyze_transaction_network(self, start_account: str):
        """
        Analyze transaction network using graph algorithms
        """
        # Perform depth-first search on transaction graph
        network_connections = self.transaction_graph.depth_first_search(start_account)

        # Calculate shortest paths
        shortest_paths = self.transaction_graph.dijkstra(start_account)

        return {
            'connected_accounts': list(network_connections),
            'path_distances': shortest_paths
        }