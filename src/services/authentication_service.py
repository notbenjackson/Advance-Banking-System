import secrets
import hashlib
import hmac
from typing import Optional
from src.core.user import User
from src.data_structures.avl_tree import AVLTree
from src.data_structures.hash_table import HashTable
from src.algorithms.search_algorithms import SearchAlgorithms

class AuthenticationService:
    def __init__(self):
        # User storage data structures
        self.user_cache = HashTable()  # Fast O(1) lookup
        self.user_tree = AVLTree()     # Efficient search and management

    def hash_password(self, password: str, salt: str) -> str:
        """
        Secure password hashing using HMAC
        """
        return hmac.new(
            salt.encode(), 
            password.encode(), 
            hashlib.sha256
        ).hexdigest()

    def verify_password(self, input_password: str, stored_hash: str, salt: str) -> bool:
        """
        Constant-time password verification
        """
        computed_hash = self.hash_password(input_password, salt)
        return hmac.compare_digest(computed_hash, stored_hash)

    def register_user(
        self, 
        username: str, 
        password: str, 
        email: str, 
        role: str = 'customer'
    ) -> Optional[User]:
        """
        User registration with advanced security
        """
        # Check if username already exists
        if self.find_user(username):
            return None

        # Generate cryptographically secure salt
        salt = secrets.token_hex(16)

        # Hash password
        password_hash = self.hash_password(password, salt)

        # Create user
        new_user = User(
            username=username,
            password_hash=password_hash,
            salt=salt,
            email=email,
            role=role
        )

        # Store in AVL Tree and Hash Table
        self.user_tree.insert_key(username, new_user)
        self.user_cache.insert(username, new_user)

        return new_user

    def authenticate(self, username: str, password: str) -> Optional[User]:
        """
        Multi-strategy user authentication
        """
        # Check cache first
        if self.user_cache.contains(username):
            user = self.user_cache.get(username)
        else:
            # Fallback to tree search
            user = self.find_user(username)

        # Verify password
        if user and self.verify_password(password, user.password_hash, user.salt):
            # Update last login
            from datetime import datetime
            user.last_login = datetime.now().isoformat()
            return user

        return None

    def find_user(self, username: str) -> Optional[User]:
        """
        Find user using multiple search strategies
        """
        # Hash Table lookup
        if self.user_cache.contains(username):
            return self.user_cache.get(username)

        # AVL Tree search
        user_node = self.user_tree.find(username)
        return user_node.value if user_node else None

    def change_password(
        self, 
        username: str, 
        old_password: str, 
        new_password: str
    ) -> bool:
        """
        Secure password change process
        """
        # Authenticate current user
        user = self.authenticate(username, old_password)
        
        if not user:
            return False

        # Generate new salt
        new_salt = secrets.token_hex(16)

        # Hash new password
        new_password_hash = self.hash_password(new_password, new_salt)

        # Update user credentials
        user.password_hash = new_password_hash
        user.salt = new_salt

        # Update in data structures
        self.user_tree.update_key(username, user)
        self.user_cache.insert(username, user)

        return True

    def list_users_by_role(self, role: str) -> list:
        """
        List users by role using tree traversal
        """
        matching_users = []

        def collect_users(node):
            if not node:
                return
            
            if node.value.role == role:
                matching_users.append(node.value)
            
            collect_users(node.left)
            collect_users(node.right)

        collect_users(self.user_tree.root)
        return matching_users

    def two_factor_authentication(
        self, 
        username: str, 
        password: str, 
        additional_factor: str
    ) -> bool:
        """
        Two-factor authentication implementation
        """
        # Standard authentication
        user = self.authenticate(username, password)
        
        if not user:
            return False

        # Additional verification logic
        # This could be extended to email, SMS, or token-based verification
        return len(additional_factor) > 6