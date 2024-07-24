import collections

with open('shops.txt') as shops_file:
    shops = list(map(lambda x: x.replace('\n', ''), shops_file.readlines()))

city_shops = {}
for line in shops:
    shop, city = line.split(':')
    city_shops[city] = shop

print(city_shops)

