import requests


class AwesomeApi:
    """
    This class implements the integration with Awesome API
    """
    HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0'}
    URL = 'https://economia.awesomeapi.com.br/json/last/%s-%s'

    def __init__(self, from_currency: str, to_currency: str):
        self.from_currency = from_currency.upper()
        self.to_currency = to_currency.upper()

    def make_request(self) -> requests.Response:
        """
        Makes a request to Awesome API and returns a dict with current value of <currency> in USD.
        """
        req = requests.get(self.URL % (self.from_currency, self.to_currency), headers=self.HEADERS)
        return req

    def converts(self, amount: float) -> float:
        """
        Converts amount of from_currency into to_currency
        """
        data = self.make_request().json()
        rate = float(data[f'{self.from_currency}{self.to_currency}']['bid'])
        return round(amount * rate, 3)
