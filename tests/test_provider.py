from faker import Faker
from faker_pk.provider import FakerPKProvider

def test_provider_registration():
    fake = Faker()
    fake.add_provider(FakerPKProvider)
    
    assert isinstance(fake.pk_male_name(), str)
    assert isinstance(fake.pk_city(), str)
            