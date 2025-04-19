import logging
import os
import sys
from typing import Optional

def setup_logging(log_level: Optional[str] = None) -> None:
    """
    Configure logging for the application.
    
    Args:
        log_level: Optional log level string (DEBUG, INFO, etc.)
                  If not provided, defaults to INFO or uses environment variable LOG_LEVEL
    """
    # Determine log level from args, env var, or default to INFO
    if log_level is None:
        log_level = os.getenv("LOG_LEVEL", "INFO").upper()
    
    numeric_level = getattr(logging, log_level, logging.INFO)
    
    # Configure logging
    logging.basicConfig(
        level=numeric_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )
    
    # Create a logger instance for this module
    logger = logging.getLogger(__name__)
    logger.info(f"Logging initialized at level: {log_level}")
