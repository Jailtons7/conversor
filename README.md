# Conversor

## Descrição

Neste projeto é criada uma API onde podemos converter montantes de dinheiro de uma moeda para outra.

Para tal foi feita uma integração com a [Awesome API](https://docs.awesomeapi.com.br/api-de-moedas).

Moedas Testadas e Suportadas:

1. DOLAR (USD)
2. REAL (BRL)
3. EURO (EUR)
4. BITCOIN (BTC)
5. ETHEREUM (ETH)

OBS.: A API de moedas Awesome API quebra para conversões
de BTC para BRL e, portanto, há esse bug por enquanto.

## Usando a API

Após baixar o código na sua máquina, instale as dependencias 
python (recomenda-se usar um ambiente virtual):

```shell
pip install -r requirements.txt
```

Rode as migrações:

```shell
./manage.py migrate
```

Sirva a aplicação:

```shell
./manage.py runserver
```

Acesse o endpoint a seguir passando os dados do seu interesse na conversão:
```shell
http://127.0.0.1:8000/api/converts?from=BRL&to=EUR&amount=25.5
```

Para a requisição anterior a resposta foi

```shell
{
    "amount": 25.5,
    "from": "BRL",
    "to": "EUR",
    "converted": 4.192
}
```

O que indica que naquele momento, 25.50 reais era equivalente a 4.19 euros.
