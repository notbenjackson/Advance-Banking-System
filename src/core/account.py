from typing import Union, List
from dataclasses import dataclass, field
from datetime import datetime
import uuid

@dataclass
class Account:
    account_number: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    customer_id: str = None
    account_type: str = 'Savings'
    balance: float = 0.0
    created_at: datetime = field(default_factory=datetime.now)
    is_active: bool = True
    overdraft_limit: float = 0.0

    def deposit(self, amount: float) -> bool:
        """
        Deposit money into the account
        
        Args:
            amount (float): Amount to deposit
        
        Returns:
            bool: True if deposit successful, False otherwise
        """
        if amount <= 0:
            return False
        
        self.balance += amount
        return True

    def withdraw(self, amount: float) -> bool:
        """
        Withdraw money from the account
        
        Args:
            amount (float): Amount to withdraw
        
        Returns:
            bool: True if withdrawal successful, False otherwise
        """
        if amount <= 0:
            return False
        
        # Check if withdrawal is possible with overdraft
        if self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
            return True
        
        return False

    def transfer(self, target_account: 'Account', amount: float) -> bool:
        """
        Transfer money to another account
        
        Args:
            target_account (Account): Destination account
            amount (float): Amount to transfer
        
        Returns:
            bool: True if transfer successful, False otherwise
        """
        if self.withdraw(amount):
            target_account.deposit(amount)
            return True
        
        return False

    def get_account_details(self) -> dict:
        """
        Get account details
        
        Returns:
            dict: Account details
        """
        return {
            'account_number': self.account_number,
            'account_type': self.account_type,
            'balance': self.balance,
            'created_at': self.created_at,
            'is_active': self.is_active
        }