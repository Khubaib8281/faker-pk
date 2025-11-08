from .personal import male_name, female_name, cnic, phone_number
from .address import city, province, full_address
from .company import company_name

class FakerPK:            
    """Generate fake Pakistani names, addresses, CNICs, phone numbers, and more."""

    def _generate_multiple(self, func, count):
        """Generate one or many values based on count."""
        if count == 1:
            return func()
        return [func() for _ in range(count)]

    def male_name(self, count=1):
        return self._generate_multiple(male_name, count)

    def female_name(self, count=1):
        return self._generate_multiple(female_name, count)

    def cnic(self, count=1):
        return self._generate_multiple(cnic, count)

    def phone_number(self, count=1):
        return self._generate_multiple(phone_number, count)

    def city(self, count=1):
        return self._generate_multiple(city, count)

    def province(self, count=1):
        return self._generate_multiple(province, count)

    def full_address(self, count=1):
        return self._generate_multiple(full_address, count)

    def company_name(self, count=1):
        return self._generate_multiple(company_name, count)

__all__ = [
    "FakerPK",
    "male_name", "female_name", "cnic", "phone_number",
    "city", "province", "full_address", "company_name"
]
