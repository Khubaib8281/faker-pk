import pytest
from faker_pk import FakerPK

@pytest.fixture
def faker_pk():
    return FakerPK()
    