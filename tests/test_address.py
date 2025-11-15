def test_city(faker_pk):
    c = faker_pk.city()
    assert isinstance(c, str)
    assert len(c) > 0

def test_province(faker_pk):
    p = faker_pk.province()
    assert isinstance(p, str)
    assert len(p) > 0

def test_full_address(faker_pk):
    addr = faker_pk.full_address()
    assert isinstance(addr, str)
    assert len(addr) > 0
    assert "," in addr
   