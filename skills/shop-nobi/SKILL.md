---
name: shop-nobi
description: Search products across online stores with Shop Nobi when a user asks to find or compare purchasable items.
---

Use the Shop Nobi MCP `search_products` tool for product discovery. Supply a nonblank `query` of at most 500 characters; optionally set integer `limit` from 1 to 20. Show the store, listed price, stock signal, and product link when present. The `url` forwards through Shop Nobi to the seller; it is not a raw merchant URL. If `paidLink` is true, show the supplied `linkLabel` beside that link. Treat prices and stock as time-sensitive, and identify missing fields rather than guessing.

Use `find_shop_nobi_page` when a user asks for a relevant Shop Nobi product-topic page. The current public server searches products, not services or other offerings. Do not claim that Shop Nobi or the user purchased, tested, or endorsed a result.

Use `get_product_details` for returned catalog descriptions, specifications, images and variant choices. Use `compare_products` for selected Nobi variant IDs, `check_price_and_availability` to recheck catalog price and stock, and `find_alternatives` for similar listings. Preserve returned shopping links and commission labels; do not invent missing facts.

## Product and variant identifiers

Read the live `tools/list` schema before calling a tool. The returned `id` is an opaque Nobi variant identifier, not a Shopify ID or SKU. Nobi `productId` and `variantId`, when exposed, identify our own parent product and selected variant.

When using a Shopify product or variant ID, always include the selling merchant's domain as `storeDomain`, for example `example.com`. Use `sourceProductId` for a Shopify parent product and `sourceVariantId` for a Shopify variant, only when the live `get_product_details` schema advertises those arguments:

```json
{"sourceProductId":"123456789","storeDomain":"example.com"}
```

```json
{"sourceVariantId":"987654321","storeDomain":"example.com"}
```

These IDs and domain are illustrative; use the actual catalog ID and merchant hostname. A known Nobi `merchantId` is an alternative merchant context where supported. SKUs also require merchant context. Never resolve source IDs or SKUs globally, guess a merchant, or put a Shopify ID into Nobi `id`, `productId` or `variantId` fields.

If the available schema accepts only `id`, use the Nobi variant ID returned by `search_products` rather than sending unsupported source-ID arguments. Comparison, price/availability and alternatives tools use returned Nobi variant IDs. A parent lookup returns variant choices; select a variant before reporting its price or stock.

[Full identifier and response guide](https://docs.nobi.ai/shop-nobi-mcp-response/).

