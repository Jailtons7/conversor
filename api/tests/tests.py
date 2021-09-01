import time

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.integrations.awesomeapi import AwesomeApi


class ApiTests(APITestCase):
    def test_integration(self):
        awesome = AwesomeApi(from_currency="USD", to_currency="BRL")
        req = awesome.make_request()
        self.assertEqual(req.status_code, status.HTTP_200_OK)

    def test_endpoint(self):
        url = reverse('api:convert')
        pairs = (
            ('BTC', 'EUR'),
            ('BTC', 'USD'),
            ('BTC', 'BRL'),
            ('BRL', 'USD'),
            ('USD', 'BRL'),
            ('EUR', 'BRL'),
            ('BRL', 'EUR'),
            ('USD', 'EUR'),
            ('EUR', 'USD'),
            ('ETH', 'USD'),
            ('ETH', 'EUR'),
            ('ETH', 'BRL'),
        )
        for pair in pairs:
            params = f'?from={pair[0]}&to={pair[1]}&amount=123.45'
            req = self.client.get(url + params)
            self.assertEqual(req.status_code, status.HTTP_200_OK)
            self.assertEqual(req.data['from'], pair[0])
            self.assertEqual(req.data['to'], pair[1])
            self.assertEqual(req.data['amount'], 123.45)
            time.sleep(0.1)  # Para evitar sobrecargas na API parceira
