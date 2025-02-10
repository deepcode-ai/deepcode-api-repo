# api/utils/helpers.py
from typing import List

def format_string(string: str) -> str:
    """Format a string to be title case."""
    return string.title()

def paginate_results(results: List, page: int = 1, per_page: int = 10):
    """Helper to paginate query results."""
    start = (page - 1) * per_page
    end = start + per_page
    return results[start:end]
