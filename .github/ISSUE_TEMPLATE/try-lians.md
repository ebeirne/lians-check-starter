---
name: Try Lians
about: The sample ticket for trying Lians. Submit it as is.
title: Add format_price for the checkout page
---
Checkout needs a `format_price(cents, currency)` helper in `pricing.py`.

Requirements:
1. USD amounts look like `$12.34`.
2. EUR amounts look like `€12.34`.
3. Refunds (negative amounts) show in parentheses, like `($5.00)`, with no minus sign.
4. Any other currency raises `ValueError`.
