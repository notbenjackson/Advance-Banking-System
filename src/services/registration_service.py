from typing import Dict, Optional
from src.core.user import User
from src.services.authentication_service import AuthenticationService
from src.data_structures.avl_tree import AVLTree
from src.data_structures.hash_table import HashTable

class UserRegistrationSchema:
    @staticmethod
    def validate(registration_data: Dict) -> Dict:
        """
        Validate user registration data
        """
        errors = {}

        # Username validation
        username = registration_data.get('username', '')
        if not username or len(username) < 3:
            errors['username'] = 'Username must be at least 3 characters'

        # Password validation
        password = registration_data.get('password', '')
        confirm_password = registration_data.get('confirm_password', '')
        if not password or len(password) < 8:
            errors['password'] = 'Password must be at least 8 characters'
        elif password != confirm_password:
            errors['confirm_password'] = 'Passwords do not match'

        # Email validation
        email = registration_data.get('email', '')
        if not email or '@' not in email:
            errors['email'] = 'Invalid email address'

        return errors

class RegistrationService:
    def __init__(self, auth_service: AuthenticationService):
        self.auth_service = auth_service
        
        # Additional data structures for user management
        self.user_registry = AVLTree()
        self.email_index = HashTable()

    def register_user(self, registration_data: Dict) -> Dict:
        """
        User registration process
        """
        # Validate registration data
        validation_errors = UserRegistrationSchema.validate(registration_data)
        if validation_errors:
            return {
                'success': False,
                'errors': validation_errors
            }

        # Check if username already exists
        username = registration_data['username']
        email = registration_data['email']

        # Check for existing username
        if self.auth_service.find_user(username):
            return {
                'success': False,
                'errors': {'username': 'Username already exists'}
            }

        # Check for existing email
        if self._find_user_by_email(email):
            return {
                'success': False,
                'errors': {'email': 'Email already registered'}
            }

        # Create user via authentication service
        new_user = self.auth_service.register_user(
            username=username,
            password=registration_data['password'],
            email=email
        )

        if new_user:
            # Additional indexing
            self.user_registry.insert_key(new_user.user_id, new_user)
            self.email_index.insert(email, new_user)

            return {
                'success': True,
                'user_id': new_user.user_id,
                'message': 'User registered successfully'
            }

        return {
            'success': False,
            'errors': {'registration': 'User registration failed'}
        }

    def _find_user_by_email(self, email: str) -> Optional[User]:
        """
        Find user by email using email index
        """
        return self.email_index.get(email) if self.email_index.contains(email) else None

    def get_users_by_criteria(self, criteria: Dict) -> list:
        """
        Retrieve users based on various criteria
        """
        matching_users = []

        def search_users(node):
            if not node:
                return
            
            user = node.value
            match = all(
                str(getattr(user, key, '')).lower() == str(value).lower()
                for key, value in criteria.items()
            )
            
            if match:
                matching_users.append(user)
            
            search_users(node.left)
            search_users(node.right)

        search_users(self.user_registry.root)
        return matching_users

# Example usage
def main():
    # Create authentication and registration services
    auth_service = AuthenticationService()
    registration_service = RegistrationService(auth_service)

    # Registration data
    registration_data = {
        'username': 'johndoe',
        'password': 'SecurePass123!',
        'confirm_password': 'SecurePass123!',
        'email': 'john.doe@example.com'
    }

    # Register user
    result = registration_service.register_user(registration_data)

    if result['success']:
        print(f"User registered successfully. User ID: {result['user_id']}")
    else:
        print("Registration failed:")
        for field, error in result.get('errors', {}).items():
            print(f"{field}: {error}")

    # Example of finding users
    admin_users = registration_service.get_users_by_criteria({
        'role': 'admin'
    })