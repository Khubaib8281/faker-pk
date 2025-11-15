import random    

# Mapping of provinces to their major cities/towns      
PROVINCE_CITIES = {
    "Punjab": [
        "Lahore", "Faisalabad", "Rawalpindi", "Multan", "Gujranwala",
        "Sialkot", "Bahawalpur", "Sargodha", "Sahiwal", "Dera Ghazi Khan"
    ],
    "Sindh": [
        "Karachi", "Hyderabad", "Sukkur", "Larkana", "Mirpur Khas",
        "Nawabshah", "Shikarpur", "Khairpur", "Jacobabad", "Thatta"
    ],
    "Khyber Pakhtunkhwa": [  
        "Peshawar", "Mardan", "Abbottabad", "Swat", "Charsadda",
        "Bannu", "Kohat", "Dera Ismail Khan", "Haripur", "Mansehra"
    ],  
    "Balochistan": [
        "Quetta", "Gwadar", "Sibi", "Khuzdar", "Turbat",
        "Chaman", "Zhob", "Bela", "Makran", "Pasni"
    ],
    "Gilgit Baltistan": [
        "Gilgit", "Skardu", "Hunza", "Ghizer", "Diamer",
        "Astore", "Shigar", "Kharmang"
    ],
    "Islamabad Capital Territory": ["Islamabad"]
}


def city_and_province():
    """Return a tuple of (city, province) based on accurate mapping."""
    province_name = random.choice(list(PROVINCE_CITIES.keys()))
    city_name = random.choice(PROVINCE_CITIES[province_name])
    return city_name, province_name


def city():
    """Return a random Pakistani city."""
    return city_and_province()[0]


def province():
    """Return the province corresponding to the random city."""
    return city_and_province()[1]


def full_address():
    """Generate a realistic full Pakistani address."""
    house_no = f"House No. {random.randint(1, 999)}"
    street = f"Street No. {random.randint(1, 30)}"
    city_name, province_name = city_and_province()
    postal_code = random.randint(10000, 99999)
    return f"{house_no}, {street}, {city_name}, {province_name}, {postal_code}"