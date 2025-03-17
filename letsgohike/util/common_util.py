"""
Module for common util
"""

import re
from typing import Any, Optional

def clean_float(value: Any) -> Optional[float]:
    """Extract and convert a valid float number from a potentially malformed string.

    Args:
        value (Any): The value that potentially contains a float number.

    Returns:
        Optional[float]: The extracted float number if found; otherwise, None.
    """
    match = re.search(r"[-+]?\d*\.?\d+", str(value))
    return float(match.group()) if match else None
