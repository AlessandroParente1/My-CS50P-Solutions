import requests

def get_exchange_rate(base_currency, target_currency):
    """
    Ottiene il tasso di cambio da una API per la conversione tra due valute.
    """
    url = f"https://api.frankfurter.app/latest?from={base_currency}&to={target_currency}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['rates'].get(target_currency, None)
    return None

def convert_currency(amount, rate):
    """
    Converte un importo utilizzando il tasso di cambio fornito 
    """
    return amount * rate

def validate_currency_code(currency_code):
    """
    Validazione del codice valuta (deve essere in formato ISO 4217, es. EUR, USD).
    """
    if len(currency_code) == 3 and currency_code.isalpha():
        return True
    return False

def main():
    """
    Funzione principale per eseguire la conversione.
    """
    base_currency = input("Enter base currency (e.g. EUR): ").upper()
    target_currency = input("Enter target currency (e.g. USD): ").upper()
    amount = float(input("Enter amount: "))
    
    if not (validate_currency_code(base_currency) and validate_currency_code(target_currency)):
        print("Invalid currency code.")
        return

    rate = get_exchange_rate(base_currency, target_currency)
    if rate:
        converted_amount = convert_currency(amount, rate)
        print(f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")
    else:
        print("Error fetching exchange rate. Please try again.")

if __name__ == "__main__":
    main()
