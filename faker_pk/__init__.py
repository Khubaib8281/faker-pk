from .personal import male_name, female_name, cnic, phone_number, sim_provider, caste, sect, dob
from .address import city, province, full_address
from .company import company_name, industry_name, iban, bank_name, salary, job_title_with_industry, job_title
from .provider import FakerPKProvider
    
    
class FakerPK:
    """Generate fake Pakistani names, addresses, CNICs, phone numbers, and more."""
    
    def _generate_multiple(self, func, count):
        """Generate one or many values based on count."""
        if count == 1:
            return func()
        return [func() for _ in range(count)]

    # --------------------
    # Personal Info
    # --------------------
    def male_name(self, count=1):
        return self._generate_multiple(male_name, count)

    def female_name(self, count=1):
        return self._generate_multiple(female_name, count)

    def cnic(self, count=1):
        return self._generate_multiple(cnic, count)

    def phone_number(self, count=1):
        return self._generate_multiple(phone_number, count)

    def sim_provider(self, count=1):
        return self._generate_multiple(sim_provider, count)

    def caste(self, count=1):
        return self._generate_multiple(caste, count)

    def sect(self, count=1):
        return self._generate_multiple(sect, count)

    def dob(self, count=1):
        return self._generate_multiple(dob, count)

    # --------------------
    # Address Info
    # --------------------
    def city(self, count=1):
        return self._generate_multiple(city, count)

    def province(self, count=1):
        return self._generate_multiple(province, count)

    def full_address(self, count=1):
        return self._generate_multiple(full_address, count)

    # --------------------
    # Company Info
    # --------------------
    def company_name(self, count=1):
        return self._generate_multiple(company_name, count)

    def industry_name(self, count=1):
        return self._generate_multiple(industry_name, count)

    def bank_name(self, count=1):
        return self._generate_multiple(bank_name, count)

    def iban(self, count=1):
        return self._generate_multiple(iban, count)

    # --------------------
    # Job Info
    # --------------------
    def job_title(self, count=1):
        return self._generate_multiple(job_title, count)

    def job_title_with_industry(self, count=1):
        return self._generate_multiple(job_title_with_industry, count)
    
    def salary(self, count=1, industry=None):
        """Generate random salary from company.py."""
        return self._generate_multiple(salary, count)     


__all__ = ["FakerPK", "FakerPKProvider"]