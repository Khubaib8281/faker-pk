import random

PREFIXES = ["Al", "Pak", "Tech", "Green", "United", "Prime", "Blue", "Smart"]
SUFFIXES = ["Traders", "Solutions", "Corporation", "Industries", "Enterprises", "Systems"]

def company_name():
    """Generate a random Pakistani-style company name."""
    return f"{random.choice(PREFIXES)} {random.choice(SUFFIXES)}"
