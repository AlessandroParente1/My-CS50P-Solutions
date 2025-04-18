import sys
import requests

# Ensure the correct argument is passed
if len(sys.argv) != 2:
    print("Usage: python bitcoin.py <number_of_bitcoins>")
    sys.exit(1)

try:
    value =float(sys.argv[1])
except ValueError:
    print(f"Error: '{arg}' is not a valid float.")
    sys.exit(1)

try:
    response = requests.get("https://api.coincap.io/v2/assets/bitcoin")
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Parse the JSON response
    data = response.json()
    bitcoin_price = float(data['data']['priceUsd'])

    total=bitcoin_price*value
    print(f"${total:,.4f}")

except requests.RequestException:
    print(f"Error: {e}")
    sys.exit(1)







