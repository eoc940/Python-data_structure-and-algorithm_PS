def solution(price, money, count):
    mul = 0
    for i in range(count):
        mul += i+1
    total_money = price * mul
    left = total_money - money
    if left > 0:
        return left
    else:
        return 0

price = 3
money = 20
count = 4
print(solution(price, money, count))
