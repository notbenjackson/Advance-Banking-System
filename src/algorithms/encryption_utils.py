import hashlib
import hmac

class EncryptionUtils:
    @staticmethod
    def hash_password(password: str, salt: str) -> str:
        """
        Secure password hashing with HMAC
        """
        return hmac.new(
            salt.encode(), 
            password.encode(), 
            hashlib.sha256
        ).hexdigest()

    @staticmethod
    def verify_password(
        input_password: str, 
        stored_hash: str, 
        salt: str
    ) -> bool:
        """
        Verify password against stored hash
        """
        computed_hash = EncryptionUtils.hash_password(input_password, salt)
        return hmac.compare_digest(computed_hash, stored_hash)