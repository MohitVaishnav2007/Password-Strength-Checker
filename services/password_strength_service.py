import logging
from typing import Dict, Any
import zxcvbn

class PasswordStrengthService:
    """
    Service to analyze the strength of passwords using the zxcvbn library.
    
    This service provides comprehensive password strength analysis including
    scoring, estimated crack times, and improvement suggestions.
    """
    
    def __init__(self):
        """Initialize the password strength service."""
        self.logger = logging.getLogger(__name__)
    
    def check_strength(self, password: str) -> Dict[str, Any]:
        """
        Check the strength of a password using zxcvbn.
        
        Args:
            password: The password to check
            
        Returns:
            Dictionary containing strength score, feedback, and crack time estimates
        """
        self.logger.info("Checking password strength")
        
        try:
            # Use zxcvbn to analyze the password
            result = zxcvbn.zxcvbn(password)
            
            # Extract relevant info from the result
            processed_result = {
                "score": result["score"],
                "feedback": result["feedback"],
                "crack_times_display": result["crack_times_display"]
            }
            
            self.logger.info(f"Password strength checked: score={result['score']}")
            return processed_result
            
        except Exception as e:
            self.logger.error(f"Error checking password strength: {str(e)}", exc_info=True)
            raise
