SYMBOLS = {"USD": "$", "EUR": "€"}


def format_price(cents: int, currency: str) -> str:
    """Format an amount in cents for display at checkout."""
    symbol = SYMBOLS[currency]
    sign = "-" if cents < 0 else ""
    cents = abs(cents)
    return f"{sign}{symbol}{cents // 100}.{cents % 100:02d}"
