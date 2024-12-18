from dataclasses import dataclass
from typing import Optional
import uuid

@dataclass
class User:
    """
    User model representing authentication details
    """
    user_id: str = str(uuid.uuid4())
    username: str = ''
    password_hash: str = ''
    salt: str = ''
    email: str = ''
    role: str = 'customer'
    is_active: bool = True
    last_login: Optional[str] = None
    created_at: Optional[str] = None

    def __post_init__(self):
        """
        Initialize default values if not provided
        """
        if not self.user_id:
            self.user_id = str(uuid.uuid4())
        
        if not self.created_at:
            from datetime import datetime
            self.created_at = datetime.now().isoformat()