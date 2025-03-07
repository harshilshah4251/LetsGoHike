import re

def clean_float(value):
    """Extracts and converts a valid float number from a potentially malformed string."""
    match = re.search(r"[-+]?\d*\.?\d+", str(value))
    return float(match.group()) if match else None
