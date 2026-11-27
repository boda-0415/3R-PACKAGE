"""Example module for the demo package"""

from .logger_config import logger


def hello_world(message):
    """Example function to say Hello world with a message"""
    logger.debug("This is DEBUG level log message")
    logger.info("This is INFO level log message")
    logger.warning("This is WARN level log message")
    logger.error("This is ERROR level log message")
    return f"Hello world!: {message}"

def calculate_mean(numbers):
    """Calculate the arithmetic mean of a list of numbers."""
    if not numbers:
        raise ValueError("The list of numbers cannot be empty.")

    return sum(numbers) / len(numbers)
