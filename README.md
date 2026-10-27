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
