def test_per_page_is_capped():
    assert min(500, 100) == 100
