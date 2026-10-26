---
name: shop-nobi
description: Search products across online stores with Shop Nobi when a user asks to find or compare purchasable items.
---

Use the Shop Nobi MCP `search_products` tool for product discovery. Supply a nonblank `query` of at most 500 characters; optionally set integer `limit` from 1 to 20. Show the store, listed price, stock signal, and product link when present. The `url` forwards through Shop Nobi to the seller; it is not a raw merchant URL. If `paidLink` is true, show the supplied `linkLabel` beside that link. Treat prices and stock as time-sensitive, and identify missing fields rather than guessing.

Use `find_shop_nobi_page` when a user asks for a relevant Shop Nobi product-topic page. The current public server searches products, not services or other offerings. Do not claim that Shop Nobi or the user purchased, tested, or endorsed a result.
