import logging
from typing import Dict, Any

from services.password_strength_service import PasswordStrengthService
from services.breach_check_service import BreachCheckService

class PasswordController:
    """
    Controller class that coordinates password strength and breach checking.
    
    This class follows the Single Responsibility Principle by delegating the actual
    checking logic to specialized service classes.
    """
    
    def __init__(self):
        """Initialize the controller with required services."""
        self.logger = logging.getLogger(__name__)
        self.strength_service = PasswordStrengthService()
        self.breach_service = BreachCheckService()
    
    def process_password(self, password: str) -> Dict[str, Any]:
        """
        Process the password by checking its strength and breach status.
        
        Args:
            password: The password to check
            
        Returns:
            A dictionary containing the combined results
        """
        self.logger.info("Processing password")
        
        try:
            # Check password strength
            strength_results = self.strength_service.check_strength(password)
            
            # Check if password has been breached
            breach_results = self.breach_service.check_breach(password)
            
            # Combine results
            combined_results = {
                "strength": strength_results,
                "breach": breach_results
            }
            
            self.logger.info("Password processed successfully")
            return combined_results
            
        except Exception as e:
            self.logger.error(f"Error processing password: {str(e)}", exc_info=True)
            raise
