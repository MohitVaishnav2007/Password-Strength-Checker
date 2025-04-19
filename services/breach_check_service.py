import hashlib
import logging
import requests
from typing import Dict, Any

class BreachCheckService:
    """
    Service to check if a password has been exposed in known data breaches
    using the HaveIBeenPwned API.
    
    This service implements the k-anonymity model for privacy protection.
    """
    
    def __init__(self):
        """Initialize the breach check service."""
        self.logger = logging.getLogger(__name__)
        self.api_url = "https://api.pwnedpasswords.com/range/{}"
        self.headers = {
            "User-Agent": "Password-Strength-Checker-Tool"
        }
    
    def check_breach(self, password: str) -> Dict[str, Any]:
        """
        Check if the password has been exposed in data breaches using HIBP API.
        
        Args:
            password: The password to check
            
        Returns:
            Dictionary containing breach status and count
        """
        self.logger.info("Checking if password has been breached")
        
        try:
            # Convert password to SHA-1 hash
            sha1hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
            prefix, suffix = sha1hash[:5], sha1hash[5:]
            
            # Make API request with the hash prefix (k-anonymity)
            response = requests.get(
                self.api_url.format(prefix),
                headers=self.headers
            )
            response.raise_for_status()
            
            # Process the response
            hash_count = self._get_hash_count(response.text, suffix)
            
            result = {
                "found": hash_count > 0,
                "count": hash_count
            }
            
            self.logger.info(f"Breach check completed: found={result['found']}, count={result['count']}")
            return result
            
        except requests.exceptions.RequestException as e:
            self.logger.error(f"API request error in breach check: {str(e)}")
            # Return a safe default on API error
            return {"found": False, "count": 0, "error": str(e)}
            
        except Exception as e:
            self.logger.error(f"Unexpected error in breach check: {str(e)}", exc_info=True)
            raise
    
    def _get_hash_count(self, response_text: str, hash_suffix: str) -> int:
        """
        Parse the API response to find if our hash suffix is present.
        
        Args:
            response_text: The text response from the HIBP API
            hash_suffix: The suffix of our SHA-1 hash to look for
            
        Returns:
            The number of times the password has been found in breaches, or 0 if not found
        """
        hash_counts = {}
        
        # Parse the response which is in format: HASH_SUFFIX:COUNT
        for line in response_text.splitlines():
            if ":" in line:
                h, count = line.split(":")
                hash_counts[h] = int(count)
        
        # Return the count if hash suffix exists, otherwise 0
        return hash_counts.get(hash_suffix, 0)
