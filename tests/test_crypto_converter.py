import unittest
from src.crypto_converter import get_crypto_price, convert_crypto_to_fiat, convert_fiat_to_crypto

class TestCryptoConverter(unittest.TestCase):
    def test_get_crypto_price(self):
        # Test fetching Bitcoin price in USD
        price = get_crypto_price("bitcoin", "usd")
        self.assertIsInstance(price, float)
        self.assertGreater(price, 0)

    def test_convert_crypto_to_fiat(self):
        # Test converting 1 Bitcoin to USD
        result = convert_crypto_to_fiat("bitcoin", 1, "usd")
        self.assertIsInstance(result, float)
        self.assertGreater(result, 0)

    def test_convert_fiat_to_crypto(self):
        # Test converting 1000 USD to Bitcoin
        result = convert_fiat_to_crypto("bitcoin", 1000, "usd")
        self.assertIsInstance(result, float)
        self.assertGreater(result, 0)

if __name__ == "__main__":
    unittest.main()
