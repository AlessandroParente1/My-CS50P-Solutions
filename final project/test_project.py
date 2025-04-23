import pytest
from project import get_exchange_rate, convert_currency, validate_currency_code

# Mocking requests.get for the exchange rate test
def test_get_exchange_rate(monkeypatch):
    def mock_get(url):
        class MockResponse:
            def json(self):
                return {"rates": {"USD": 1.10}}
            @property
            def status_code(self):
                return 200
        return MockResponse()
    
    monkeypatch.setattr("requests.get", mock_get)
    rate = get_exchange_rate("EUR", "USD")
    assert rate == 1.10

def test_convert_currency():
    result = convert_currency(100, 1.10)
    assert result == 110.00  # (100 * 1.10)

def test_validate_currency_code():
    assert validate_currency_code("USD") == True
    assert validate_currency_code("US") == False
    assert validate_currency_code("usd") == False
    assert validate_currency_code("123") == False
