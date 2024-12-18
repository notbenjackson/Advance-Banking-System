from dataclasses import dataclass
from typing import Optional
import re

@dataclass
class UserRegistrationSchema:
    """
    Data validation schema for user registration
    """
    username: str
    password: str
    confirm_password: str
    email: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone_number: Optional[str] = None

    def validate(self) -> dict:
        """
        Comprehensive validation for registration data
        
        Returns:
            dict: Validation errors or empty dict if valid
        """
        errors = {}

        # Username validation
        if not self.username:
            errors['username'] = 'Username is required'
        elif len(self.username) < 3:
            errors['username'] = 'Username must be at least 3 characters'
        elif not re.match(r'^[a-zA-Z0-9_]+$', self.username):
            errors['username'] = 'Username can only contain letters, numbers, and underscores'

        # Password validation
        if not self.password:
            errors['password'] = 'Password is required'
        elif len(self.password) < 8:
            errors['password'] = 'Password must be at least 8 characters'
        elif not re.search(r'[A-Z]', self.password):
            errors['password'] = 'Password must contain at least one uppercase letter'
        elif not re.search(r'[0-9]', self.password):
            errors['password'] = 'Password must contain at least one number'
        elif not re.search(r'[!@#$%^&*(),.?":{}|<>]', self.password):
            errors['password'] = 'Password must contain at least one special character'

        # Password confirmation
        if self.password != self.confirm_password:
            errors['confirm_password'] = 'Passwords do not match'

        # Email validation
        if not self.email:
            errors['email'] = 'Email is required'
        elif not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', self.email):
            errors['email'] = 'Invalid email format'

        # Optional phone number validation
        if self.phone_number:
            if not re.match(r'^\+?1?\d{10,14}$', self.phone_number):
                errors['phone_number'] = 'Invalid phone number format'

        return errors