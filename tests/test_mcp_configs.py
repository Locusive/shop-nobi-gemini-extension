"""Check package connections offline without executing either AI client."""

import json
from pathlib import Path
import unittest
from urllib.parse import parse_qs, urlsplit


ROOT = Path(__file__).resolve().parents[1]


class McpConfigurationTest(unittest.TestCase):
    """Preserve source labels independently of the installed client's identity."""

    def test_installed_connections_preserve_transport_and_client_identity(self):
        """Both packages keep their supported URL field and existing header."""
        configurations = [
            ("gemini-extension.json", "httpUrl", "gemini_extension", "shop-nobi-gemini-cli"),
            ("mcp_config.json", "serverUrl", "antigravity_plugin", "shop-nobi-antigravity"),
        ]
        for filename, field, source, client in configurations:
            with self.subTest(package=source):
                server = json.loads((ROOT / filename).read_text())["mcpServers"]["shop-nobi"]
                url = urlsplit(server[field])
                self.assertEqual((url.scheme, url.netloc, url.path), ("https", "api.nobi.ai", "/v1/shop/mcp"))
                self.assertEqual(parse_qs(url.query), {"source": [source]})
                self.assertEqual(url.fragment, "")
                self.assertEqual(server["headers"]["x-nobi-mcp-client"], client)


if __name__ == "__main__":
    unittest.main()
