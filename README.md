# Shop Nobi for Antigravity and Gemini CLI

Connect an AI agent to the [Shop Nobi search engine](https://nobi.ai/shop/mcp). The current public MCP server searches products across online stores and returns product names, stores, prices, availability, images, and links to the merchant. It is read-only and does not require an account or API key.

## Install in Antigravity CLI

```sh
agy plugin install https://github.com/Locusive/shop-nobi-gemini-extension
```

Ask for a product search, for example: “Find a merino wool cardigan under $200 and show the store, price, and product link for each result.” The native plugin provides the Shop Nobi MCP server and a short product-search skill. Antigravity may ask you to approve the tool call.

## Install in Gemini CLI

```sh
gemini extensions install https://github.com/Locusive/shop-nobi-gemini-extension
```

Restart Gemini CLI, then ask for a product search, for example: “Find a merino wool cardigan under $200 and show the store, price, and product link for each result.” Gemini CLI can call the `search_products` tool when the request fits. It may ask you to approve the tool call.

The extension also exposes `find_shop_nobi_page` for relevant Shop Nobi product-topic pages. Prices and availability can change, so confirm them at the merchant before buying. Search results are not endorsements or fit guarantees.

## Connection

Both packages connect to `https://api.nobi.ai/v1/shop/mcp` using MCP Streamable HTTP. Gemini CLI adds `?source=gemini_extension`; Antigravity adds `?source=antigravity_plugin`. These labels identify the installed configuration in Nobi analytics, separately from the client name. A copied configuration keeps its label; it does not prove where someone first found Shop Nobi.

Neither package runs a local server or asks for credentials. See the [Shop Nobi connector guide](https://docs.nobi.ai/shop-nobi-connector/) for setup and the [plain Markdown guide](https://nobi.ai/shop-nobi-mcp.md) for tool arguments and response fields.

This extension currently supports product search. Shop Nobi's broader vision includes search for other online offerings, but those are not exposed by this MCP server yet.

## Maintainer

[Locusive](https://github.com/Locusive) maintains Shop Nobi. Report connection or result issues through this repository's Issues tab.

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

