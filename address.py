import random

CITIES = [
    "Lahore", "Karachi", "Islamabad", "Rawalpindi", "Faisalabad",
    "Multan", "Peshawar", "Quetta", "Hyderabad", "Sialkot", "Gujranwala"
]

PROVINCES = ["Punjab", "Sindh", "Khyber Pakhtunkhwa", "Balochistan", "Gilgit Baltistan"]

def city():     
    """Return a random Pakistani city."""
    return random.choice(CITIES)

def province():
    """Return a random Pakistani province."""
    return random.choice(PROVINCES)

def full_address():
    """Generate a random full Pakistani address."""
    house_no = f"House No. {random.randint(1, 999)}"
    street = f"Street No. {random.randint(1, 30)}"
    city_name = city()
    province_name = province()
    postal_code = random.randint(10000, 99999)
    return f"{house_no}, {street}, {city_name}, {province_name}, {postal_code}"
