import collections

num_shoes = int(input())
stock = collections.Counter(map(int, input().split()))

income = 0

for _ in range(int(input())):
    ss, price = map(int,input().split())
    if stock[ss]:
        stock[ss]-=1
        income+=price
print(income)
