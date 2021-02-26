price_list = input().split(';')
prices = [int(price) for price in price_list]
prices.sort(reverse=True)

for i in prices:
    print(f'{i:9,}')
