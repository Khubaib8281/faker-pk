def test_male_name(faker_pk):
    name = faker_pk.male_name()
    assert isinstance(name, str)
    assert len(name) > 0

def test_female_name(faker_pk):
    name = faker_pk.female_name()
    assert isinstance(name, str)
    assert len(name) > 0

def test_cnic(faker_pk):
    c = faker_pk.cnic()
    assert isinstance(c, str)
    assert len(c) == 15   # 13 digits + 2 hyphens
    assert c[5] == "-"
    assert c[13] == "-"
    