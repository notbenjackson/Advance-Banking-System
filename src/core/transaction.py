from typing import Optional
from dataclasses import dataclass, field
from datetime import datetime
import uuid

@dataclass
class Transaction:
    transaction_id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    from_account: Optional[str] = None
    to_account: Optional[str] = None
    amount: float = 0.0
    transaction_type: str = 'TRANSFER'
    timestamp: datetime = field(default_factory=datetime.now)
    status: str = 'PENDING'

    def complete_transaction(self) -> bool:
        """
        Mark transaction as completed
        
        Returns:
            bool: True if transaction can be completed
        """
        if self.amount > 0 and self.from_account and self.to_account:
            self.status = 'COMPLETED'
            return True
        
        self.status = 'FAILED'
        return False

    def get_transaction_details(self) -> dict:
        """
        Get transaction details
        
        Returns:
            dict: Transaction details
        """
        return {
            'transaction_id': self.transaction_id,
            'from_account': self.from_account,
            'to_account': self.to_account,
            'amount': self.amount,
            'transaction_type': self.transaction_type,
            'timestamp': self.timestamp,
            'status': self.status
        }

    @classmethod
    def create_transaction(
        cls, 
        from_account: str, 
        to_account: str, 
        amount: float, 
        transaction_type: str = 'TRANSFER'
    ) -> 'Transaction':
        """
        Create a new transaction
        
        Args:
            from_account (str): Source account
            to_account (str): Destination account
            amount (float): Transaction amount
            transaction_type (str): Type of transaction
        
        Returns:
            Transaction: New transaction instance
        """
        return cls(
            from_account=from_account,
            to_account=to_account,
            amount=amount,
            transaction_type=transaction_type
        )