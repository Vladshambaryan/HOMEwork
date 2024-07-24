def progression(limit=100):
    n = 2
    num = n
    count = 1
    while count < limit:
        yield num
        num += n
        count += 1

for number in progression(100):
    print(number)
print(list(progression(100)))

count = 1
for number in progression(10000000000000000000000000000000000):
    if count == 1000000:
        print(number)
        break
    count += 1





















