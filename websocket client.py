# # https://github.com/websocket-client/websocket-client
# from websocket import create_connection
# options = {}
# options['origin'] = 'https://exchange.blockchain.com'
# url = "wss://ws.blockchain.info/mercury-gateway/v1/ws"
# ws = create_connection(url, **options)
# msg = '{"token": "{API_SECRET}", "action": "subscribe", "channel": "auth"}'
# ws.send(msg)
# result =  ws.recv()
# print(result)
# # { "seqnum":0,
# #   "event":"subscribed",
# #   "channel":"auth",
# #   "readOnly":false }
# ws.close()


data = {
    "USD": {
        "15m": 57527.96,
        "last": 57527.96,
        "buy": 57527.96,
        "sell": 57527.96,
        "symbol": "$"
    },
    "AUD": {
        "15m": 74266.92,
        "last": 74266.92,
        "buy": 74266.92,
        "sell": 74266.92,
        "symbol": "$"
    },
    "BRL": {
        "15m": 308021.94,
        "last": 308021.94,
        "buy": 308021.94,
        "sell": 308021.94,
        "symbol": "R$"
    },
    "CAD": {
        "15m": 70575.82,
        "last": 70575.82,
        "buy": 70575.82,
        "sell": 70575.82,
        "symbol": "$"
    },
    "CHF": {
        "15m": 52518.59,
        "last": 52518.59,
        "buy": 52518.59,
        "sell": 52518.59,
        "symbol": "CHF"
    },
    "CLP": {
        "15m": 40562936,
        "last": 40562936,
        "buy": 40562936,
        "sell": 40562936,
        "symbol": "$"
    },
    "CNY": {
        "15m": 372412.98,
        "last": 372412.98,
        "buy": 372412.98,
        "sell": 372412.98,
        "symbol": "¥"
    },
    "DKK": {
        "15m": 356309.64,
        "last": 356309.64,
        "buy": 356309.64,
        "sell": 356309.64,
        "symbol": "kr"
    },
    "EUR": {
        "15m": 47812.33,
        "last": 47812.33,
        "buy": 47812.33,
        "sell": 47812.33,
        "symbol": "€"
    },
    "GBP": {
        "15m": 41364.1,
        "last": 41364.1,
        "buy": 41364.1,
        "sell": 41364.1,
        "symbol": "£"
    },
    "HKD": {
        "15m": 446934.12,
        "last": 446934.12,
        "buy": 446934.12,
        "sell": 446934.12,
        "symbol": "$"
    },
    "INR": {
        "15m": 4245425.15,
        "last": 4245425.15,
        "buy": 4245425.15,
        "sell": 4245425.15,
        "symbol": "₹"
    },
    "ISK": {
        "15m": 7246604.99,
        "last": 7246604.99,
        "buy": 7246604.99,
        "sell": 7246604.99,
        "symbol": "kr"
    },
    "JPY": {
        "15m": 6275199.3,
        "last": 6275199.3,
        "buy": 6275199.3,
        "sell": 6275199.3,
        "symbol": "¥"
    },
    "KRW": {
        "15m": 64719588.28,
        "last": 64719588.28,
        "buy": 64719588.28,
        "sell": 64719588.28,
        "symbol": "₩"
    },
    "NZD": {
        "15m": 79768.15,
        "last": 79768.15,
        "buy": 79768.15,
        "sell": 79768.15,
        "symbol": "$"
    },
    "PLN": {
        "15m": 219172.48,
        "last": 219172.48,
        "buy": 219172.48,
        "sell": 219172.48,
        "symbol": "zł"
    },
    "RUB": {
        "15m": 4303165.96,
        "last": 4303165.96,
        "buy": 4303165.96,
        "sell": 4303165.96,
        "symbol": "RUB"
    },
    "SEK": {
        "15m": 488034.05,
        "last": 488034.05,
        "buy": 488034.05,
        "sell": 488034.05,
        "symbol": "kr"
    },
    "SGD": {
        "15m": 76849.01,
        "last": 76849.01,
        "buy": 76849.01,
        "sell": 76849.01,
        "symbol": "$"
    },
    "THB": {
        "15m": 1790385.07,
        "last": 1790385.07,
        "buy": 1790385.07,
        "sell": 1790385.07,
        "symbol": "฿"
    },
    "TRY": {
        "15m": 478908.74,
        "last": 478908.74,
        "buy": 478908.74,
        "sell": 478908.74,
        "symbol": "₺"
    },
    "TWD": {
        "15m": 1604627.36,
        "last": 1604627.36,
        "buy": 1604627.36,
        "sell": 1604627.36,
        "symbol": "NT$"
    }
}
for i in data:
    print(i) 
    
    
    "timestamp":1.667854081E12,
    "market_price_usd":20843.99,
    "hash_rate":2.5767169297761053E11,
    "total_fees_btc":-88125000000,
    "n_btc_mined":88125000000,
    "n_tx":250365,
    "n_blocks_mined":141,
    "minutes_between_blocks":9.2,
    "totalbc":1920103750000000,
    "n_blocks_total":762166,
    "estimated_transaction_volume_usd":3.4843425726628633E9,
    "blocks_size":165474886,
    "miners_revenue_usd":0.0,
    "nextretarget":764063,
    "difficulty":36762198818467,
    "estimated_btc_sent":16716293630264,
    "miners_revenue_btc":0,
    "total_btc_sent":421895469977039,
    "trade_volume_btc":5037.74,
    "trade_volume_usd":1.050066021826E8}