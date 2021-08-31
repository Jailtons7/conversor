import requests


class AwesomeApi:
    """
    This class implements the integration with Awesome API
    """
    HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0'}
    URL = 'https://economia.awesomeapi.com.br/json/last/%s-USD'

    def __init__(self, from_currency: str, to_currency: str):
        self.from_currency = from_currency.upper()
        self.to_currency = to_currency.upper()

    def make_request(self, currency: str) -> requests.Response:
        """
        Makes a request to Awesome API and returns a dict with current value of <currency> in USD.
        """
        req = requests.get(self.URL % currency, headers=self.HEADERS)
        return req

    def converts(self, amount: float) -> float:
        """
        Converts amount of from_currency into to_currency
        """
        from_currency = self.make_request(self.from_currency)
        to_currency = self.make_request(self.to_currency)
        from_currency_bid = float(from_currency.json()[f'{self.from_currency}USD']['bid'])
        to_currency_bid = float(to_currency.json()[f'{self.to_currency}USD']['bid'])
        return amount * from_currency_bid / to_currency_bid
