from src.utils.data_structure_utils import DataStructureManager, AlgorithmUtility

class AnalyticsService:
    def __init__(self):
        self.data_manager = DataStructureManager()

    def analyze_customer_network(self, customer_id):
        """
        Perform network analysis for a customer
        """
        # Find customer's network connections
        connections = self.data_manager.network_graph.depth_first_search(customer_id)
        
        # Calculate shortest paths
        shortest_paths = self.data_manager.network_graph.dijkstra(customer_id)

        return {
            'direct_connections': list(connections),
            'path_distances': shortest_paths
        }

    def transaction_priority_analysis(self, transactions):
        """
        Prioritize transactions based on amount and risk
        """
        for transaction in transactions:
            # Prioritize based on transaction amount
            priority = self._calculate_transaction_priority(transaction)
            self.data_manager.prioritize_transaction(transaction, priority)

        # Process high-priority transactions
        while not self.data_manager.transaction_queue.is_empty():
            top_transaction = self.data_manager.transaction_queue.pop()
            # Process transaction logic here

    def _calculate_transaction_priority(self, transaction):
        """
        Calculate transaction priority based on amount and risk factors
        """
        base_priority = transaction.amount
        
        # Add risk factors
        if transaction.transaction_type == 'INTERNATIONAL':
            base_priority += 100
        
        if transaction.amount > 10000:
            base_priority += 50
        
        return base_priority

class RiskAnalysisService:
    def __init__(self):
        self.data_manager = DataStructureManager()

    def detect_suspicious_activity(self, customer_transactions):
        """
        Use graph and search algorithms to detect suspicious activities
        """
        # Analyze transaction patterns
        transaction_analysis = AlgorithmUtility.analyze_transactions(customer_transactions)
        
        # Detect unusual transaction patterns
        suspicious_transactions = []
        for transaction in transaction_analysis['sorted_by_amount']:
            if self._is_suspicious_transaction(transaction):
                suspicious_transactions.append(transaction)

        return suspicious_transactions

    def _is_suspicious_transaction(self, transaction):
        """
        Implement complex transaction suspicion logic
        """
        # Example suspicious transaction criteria
        return (
            transaction.amount > 50000 or  # Large transaction
            transaction.transaction_type == 'INTERNATIONAL'  # Cross-border transaction
        )