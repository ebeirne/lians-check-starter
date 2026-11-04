from pricing import format_price


def test_usd():
    assert format_price(1234, "USD") == "$12.34"


def test_eur():
    assert format_price(1234, "EUR") == "€12.34"
