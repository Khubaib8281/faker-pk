from faker.providers import BaseProvider    
import random   
from .personal import (
    male_name, female_name, cnic, phone_number, sim_provider, caste, sect, dob
)
from .address import city, province, full_address
from .company import (
    company_name, industry_name, job_title, job_title_with_industry,
    salary, bank_name, iban
)   


class FakerPKProvider(BaseProvider):
    """Faker provider for Pakistani personal info, addresses, companies, jobs, and more."""

    # --------------------
    # Personal Info
    # --------------------
    def pk_male_name(self, count=1):
        if count == 1:
            return male_name()
        return [male_name() for _ in range(count)]

    def pk_female_name(self, count=1):
        if count == 1:
            return female_name()
        return [female_name() for _ in range(count)]

    def pk_cnic(self, count=1):
        if count == 1:
            return cnic()
        return [cnic() for _ in range(count)]

    def pk_phone_number(self, count=1):
        if count == 1:
            return phone_number()
        return [phone_number() for _ in range(count)]

    def pk_sim_provider(self, count=1):
        if count == 1:
            return sim_provider()
        return [sim_provider() for _ in range(count)]

    def pk_caste(self, count=1):
        if count == 1:
            return caste()
        return [caste() for _ in range(count)]

    def pk_sect(self, count=1):
        if count == 1:
            return sect()
        return [sect() for _ in range(count)]

    def pk_dob(self, count=1):
        if count == 1:
            return dob()
        return [dob() for _ in range(count)]

    # --------------------
    # Address Info
    # --------------------
    def pk_city(self, count=1):
        if count == 1:
            return city()
        return [city() for _ in range(count)]

    def pk_province(self, count=1):
        if count == 1:
            return province()
        return [province() for _ in range(count)]

    def pk_full_address(self, count=1):
        if count == 1:
            return full_address()
        return [full_address() for _ in range(count)]

    # --------------------
    # Company Info
    # --------------------
    def pk_company_name(self, count=1):
        if count == 1:
            return company_name()
        return [company_name() for _ in range(count)]

    def pk_industry_name(self, count=1):
        if count == 1:
            return industry_name()
        return [industry_name() for _ in range(count)]

    def pk_job_title(self, count=1, industry=None):
        if count == 1:
            return job_title(industry=industry)
        return [job_title(industry=industry) for _ in range(count)]

    def pk_job_title_with_industry(self, count=1):
        if count == 1:
            return job_title_with_industry()
        return [job_title_with_industry() for _ in range(count)]

    def pk_salary(self, count=1, industry=None):
        if count == 1:
            return salary(industry=industry)
        return [salary(industry=industry) for _ in range(count)]

    def pk_bank_name(self, count=1):
        if count == 1:
            return bank_name()
        return [bank_name() for _ in range(count)]

    def pk_iban(self, count=1):
        if count == 1:
            return iban()
        return [iban() for _ in range(count)]
    