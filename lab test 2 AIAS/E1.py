def update_stock(stock, sold):
    for item in sold:
        stock[item] = stock[item] - sold[item]  
    return stock

stock = {"Shoes": 10, "Socks": 20}
sold = {"Shoes": 2, "Socks": 5}
print(update_stock(stock, sold))