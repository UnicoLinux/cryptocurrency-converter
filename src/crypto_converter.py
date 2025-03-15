import requests

def get_crypto_price(crypto_id, currency):
    """
    Fetches the current price of a cryptocurrency in a specified currency using the CoinGecko API.
    """
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies={currency}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        if crypto_id in data:
            return data[crypto_id][currency]
        else:
            print(f"Error: Cryptocurrency '{crypto_id}' not found.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Connection error: {e}")
        return None

def convert_crypto_to_fiat(crypto_id, amount, currency):
    """
    Converts a given amount of cryptocurrency to fiat currency.
    """
    price = get_crypto_price(crypto_id, currency)
    if price is not None:
        return amount * price
    else:
        return None

def convert_fiat_to_crypto(crypto_id, amount, currency):
    """
    Converts a given amount of fiat currency to cryptocurrency.
    """
    price = get_crypto_price(crypto_id, currency)
    if price is not None:
        return amount / price
    else:
        return None

def show_current_prices(currency):
    """
    Displays the current prices of popular cryptocurrencies in the specified currency.
    """
    cryptocurrencies = ["bitcoin", "ethereum", "litecoin", "ripple", "dogecoin"]
    print(f"\nCurrent cryptocurrency prices (in {currency.upper()}):")
    for crypto in cryptocurrencies:
        price = get_crypto_price(crypto, currency)
        if price is not None:
            print(f"- {crypto.capitalize()}: {price:.2f} {currency.upper()}")

def display_menu():
    """
    Displays the main menu options.
    """
    print("\nOptions:")
    print("1. Convert from cryptocurrency to fiat")
    print("2. Convert from fiat to cryptocurrency")
    print("3. Show current cryptocurrency prices")
    print("4. Exit")

def main():
    print("""
    ==============================================
    Cryptocurrency Converter
    ==============================================
    Convert cryptocurrencies to fiat currencies and vice versa.
    Uses real-time data from CoinGecko API.
    ==============================================
    """)

    while True:
        display_menu()
        choice = input("Select an option (1-4): ")

        if choice == "1":
            crypto_id = input("Enter the cryptocurrency (e.g., btc, eth, ltc): ").lower()
            amount = float(input("Enter the amount: "))
            currency = input("Enter the fiat currency (e.g., eur, usd, gbp): ").lower()
            result = convert_crypto_to_fiat(crypto_id, amount, currency)
            if result is not None:
                print(f"\nResult: {amount} {crypto_id.upper()} = {result:.2f} {currency.upper()}")
            else:
                print("Error: Unable to complete the conversion.")

        elif choice == "2":
            crypto_id = input("Enter the cryptocurrency (e.g., btc, eth, ltc): ").lower()
            amount = float(input("Enter the amount: "))
            currency = input("Enter the fiat currency (e.g., eur, usd, gbp): ").lower()
            result = convert_fiat_to_crypto(crypto_id, amount, currency)
            if result is not None:
                print(f"\nResult: {amount} {currency.upper()} = {result:.8f} {crypto_id.upper()}")
            else:
                print("Error: Unable to complete the conversion.")

        elif choice == "3":
            currency = input("Enter the fiat currency to display prices (e.g., eur, usd, gbp): ").lower()
            show_current_prices(currency)

        elif choice == "4":
            print("\nThank you for using the Cryptocurrency Converter. Goodbye!")
            break

        else:
            print("\nError: Invalid option. Please try again.")

if __name__ == "__main__":
    main()
