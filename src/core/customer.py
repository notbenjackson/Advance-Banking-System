from typing import List, Optional
from dataclasses import dataclass, field
import uuid
from datetime import datetime

@dataclass
class Customer:
    customer_id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    first_name: str = None
    last_name: str = None
    email: str = None
    phone_number: str = None
    address: str = None
    date_of_birth: Optional[datetime] = None
    registration_date: datetime = field(default_factory=datetime.now)
    accounts: List[str] = field(default_factory=list)
    is_active: bool = True

    def add_account(self, account_number: str) -> bool:
        """
        Add a new account to customer's profile
        
        Args:
            account_number (str): Account number to add
        
        Returns:
            bool: True if account added successfully
        """
        if account_number not in self.accounts:
            self.accounts.append(account_number)
            return True
        return False

    def remove_account(self, account_number: str) -> bool:
        """
        Remove an account from customer's profile
        
        Args:
            account_number (str): Account number to remove
        
        Returns:
            bool: True if account removed successfully
        """
        if account_number in self.accounts:
            self.accounts.remove(account_number)
            return True
        return False

    def get_customer_details(self) -> dict:
        """
        Get customer details
        
        Returns:
            dict: Customer details
        """
        return {
            'customer_id': self.customer_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'phone_number': self.phone_number,
            'accounts': self.accounts,
            'is_active': self.is_active
        }

    @property
    def full_name(self) -> str:
        """
        Get full name of customer
        
        Returns:
            str: Full name
        """
        return f"{self.first_name} {self.last_name}"