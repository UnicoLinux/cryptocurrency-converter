import requests

# Dictionary to convert abbreviations to CoinGecko official names
CRYPTO_ALIASES = {
    "btc": "bitcoin",
    "eth": "ethereum",
    "ltc": "litecoin",
    "xrp": "ripple",
    "doge": "dogecoin"
}

# Supported fiat currencies
SUPPORTED_FIAT = {"usd", "eur", "gbp"}

def get_crypto_price(crypto_id, currency):
    """
    Fetches the current price of a cryptocurrency in a specified fiat currency using the CoinGecko API.
    """
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies={currency}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an error for HTTP issues
        data = response.json()
        return data.get(crypto_id, {}).get(currency)  # Returns price or None if not found
    except requests.exceptions.RequestException as e:
        print(f"Connection error: {e}")
        return None

def convert_crypto_to_fiat(crypto_id, amount, currency):
    """
    Converts a given amount of cryptocurrency to fiat currency.
    """
    price = get_crypto_price(crypto_id, currency)
    return amount * price if price is not None else None

def convert_fiat_to_crypto(crypto_id, amount, currency):
    """
    Converts a given amount of fiat currency to cryptocurrency.
    """
    price = get_crypto_price(crypto_id, currency)
    return amount / price if price is not None else None

def show_current_prices(currency):
    """
    Displays the current prices of popular cryptocurrencies in the specified fiat currency.
    """
    cryptocurrencies = ["bitcoin", "ethereum", "litecoin", "ripple", "dogecoin"]
    
    print(f"\nCurrent cryptocurrency prices (in {currency.upper()}):")
    for crypto in cryptocurrencies:
        price = get_crypto_price(crypto, currency)
        if price is not None:
            print(f"- {crypto.capitalize()}: {price:.2f} {currency.upper()}")
        else:
            print(f"- {crypto.capitalize()}: Price not available.")

def display_menu():
    """
    Displays the main menu.
    """
    print("\nOptions:")
    print("1. Convert cryptocurrency to fiat")
    print("2. Convert fiat to cryptocurrency")
    print("3. Show current cryptocurrency prices")
    print("4. Exit")

def main():
    print("""
    ==============================================
    CRYPTOCURRENCY CONVERTER
    ==============================================
    Convert cryptocurrencies to fiat currencies and vice versa.
    Uses real-time data from the CoinGecko API.
    ==============================================
    """)

    while True:
        display_menu()
        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            crypto_id = input("Enter the cryptocurrency (e.g., btc, eth, ltc): ").lower()
            crypto_id = CRYPTO_ALIASES.get(crypto_id, crypto_id)  # Convert alias

            if crypto_id not in CRYPTO_ALIASES.values():
                print("Error: Unsupported cryptocurrency.")
                continue

            try:
                amount = float(input("Enter the amount: "))
                currency = input("Enter the fiat currency (usd, eur, gbp): ").lower()

                if currency not in SUPPORTED_FIAT:
                    print("Error: Unsupported currency.")
                    continue

                result = convert_crypto_to_fiat(crypto_id, amount, currency)
                if result is not None:
                    print(f"\nResult: {amount} {crypto_id.upper()} = {result:.2f} {currency.upper()}")
                else:
                    print("Error: Unable to complete the conversion.")

            except ValueError:
                print("Error: Please enter a valid numeric value.")

        elif choice == "2":
            crypto_id = input("Enter the cryptocurrency (e.g., btc, eth, ltc): ").lower()
            crypto_id = CRYPTO_ALIASES.get(crypto_id, crypto_id)  # Convert alias

            if crypto_id not in CRYPTO_ALIASES.values():
                print("Error: Unsupported cryptocurrency.")
                continue

            try:
                amount = float(input("Enter the amount in fiat currency: "))
                currency = input("Enter the fiat currency (usd, eur, gbp): ").lower()

                if currency not in SUPPORTED_FIAT:
                    print("Error: Unsupported currency.")
                    continue

                result = convert_fiat_to_crypto(crypto_id, amount, currency)
                if result is not None:
                    print(f"\nResult: {amount} {currency.upper()} = {result:.8f} {crypto_id.upper()}")
                else:
                    print("Error: Unable to complete the conversion.")

            except ValueError:
                print("Error: Please enter a valid numeric value.")

        elif choice == "3":
            currency = input("Enter the fiat currency to display prices (usd, eur, gbp): ").lower()

            if currency not in SUPPORTED_FIAT:
                print("Error: Unsupported currency.")
                continue

            show_current_prices(currency)

        elif choice == "4":
            print("\nThank you for using the Cryptocurrency Converter. Goodbye!")
            break

        else:
            print("\nError: Invalid option. Please try again.")

if __name__ == "__main__":
    main()
