# 주유소

import sys

city = int(sys.stdin.readline())
length = list(map(int, sys.stdin.readline().split()))
oil_price = list(map(int, sys.stdin.readline().split()))

price = oil_price[0]
answer = 0

for i, v in enumerate(oil_price[:-1]):
    if v < price :
        price = v
    answer += length[i] * price

print(answer)

