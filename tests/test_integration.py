def test_end_to_end_generation(faker_pk):
    assert isinstance(faker_pk.full_address(), str)
    assert isinstance(faker_pk.phone_number(), str)
    assert isinstance(faker_pk.company_name(), str)
    assert isinstance(faker_pk.job_title(), str) or isinstance(faker_pk.job_title_with_industry(), str)
    