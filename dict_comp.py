# dictionary comprehension
# {key:value for (key, value) in dict.items() if condition}

stocks = {
    'AAPL': 121,
    'AMZN': 3380,
    'MSFT': 219,
    'BIIB': 280,
    'QDEL': 266,
    'LVGO': 144
}


new_stocks = {symbol:price*1.02 for (symbol, price) in stocks.items()}
print(new_stocks)

selected_stocks = {s:p for (s, p) in stocks.items() if p>200}
print(selected_stocks)