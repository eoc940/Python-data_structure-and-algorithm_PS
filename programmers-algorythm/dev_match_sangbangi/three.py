# 다단계 칫솔 판매

def solution(enroll, referral, seller, amount):
    answer = []
    relationship = dict()
    for under, upper in zip(enroll, referral):
        if upper != "-":
            relationship[under] = [0, upper]
        else:
            relationship[under] = [0, "center"]


    for sell_people, brush in zip(seller, amount):
        price = brush * 100
        while sell_people != "center" and price > 0:
            upper_money = int(price / 10)
            price -= upper_money
            relationship[sell_people][0] += price
            sell_people = relationship[sell_people][1]
            price = upper_money


    for person in enroll:
        answer.append(relationship[person][0])

    return answer

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]
print(solution(enroll, referral, seller, amount))
