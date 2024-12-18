import secrets
import hashlib
import hmac
from typing import Optional
from src.core.user import User
from src.data_structures.avl_tree import AVLTree
from src.data_structures.hash_table import HashTable

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
        # Normalize username to lowercase for consistency
        username = username.lower()

        # Check if username already exists
        if self.find_user(username):
            print(f"Debug: Username '{username}' already exists.")
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

        print(f"Debug: User '{username}' registered successfully.")
        return new_user

    def authenticate(self, username: str, password: str) -> Optional[User]:
        """
        Multi-strategy user authentication
        """
        username = username.lower()  # Normalize username

        print(f"Debug: Authenticating username '{username}'")

        # Check cache first
        if self.user_cache.contains(username):
            user = self.user_cache.get(username)
            print(f"Debug: User '{username}' found in cache.")
        else:
            # Fallback to tree search
            user = self.find_user(username)
            if user:
                print(f"Debug: User '{username}' found in AVL tree.")
            else:
                print(f"Debug: User '{username}' not found.")
                return None

        # Verify password
        if self.verify_password(password, user.password_hash, user.salt):
            print(f"Debug: Password verified for user '{username}'.")
            return user

        print(f"Debug: Password verification failed for user '{username}'.")
        return None

    def find_user(self, username: str) -> Optional[User]:
        """
        Find user using multiple search strategies
        """
        username = username.lower()  # Normalize username

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
        username = username.lower()  # Normalize username

        # Authenticate current user
        user = self.authenticate(username, old_password)
        
        if not user:
            print(f"Debug: Authentication failed for password change for user '{username}'.")
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

        print(f"Debug: Password changed successfully for user '{username}'.")
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
        print(f"Debug: Found {len(matching_users)} users with role '{role}'.")
        return matching_users

    def save_users_to_file(self, file_path="users.json"):
        """
        Save users to a file for persistence
        """
        import json
        users = {
            username: user.to_dict() for username, user in self.user_cache.get_all_items()
        }
        with open(file_path, "w") as f:
            json.dump(users, f)
        print("Debug: Users saved to file.")

    def load_users_from_file(self, file_path="users.json"):
        """
        Load users from a file for persistence
        """
        import json
        try:
            with open(file_path, "r") as f:
                users = json.load(f)
            for username, user_data in users.items():
                user = User.from_dict(user_data)
                self.user_cache.insert(username, user)
                self.user_tree.insert_key(username, user)
            print("Debug: Users loaded from file.")
        except FileNotFoundError:
            print("Debug: No user data file found.")
