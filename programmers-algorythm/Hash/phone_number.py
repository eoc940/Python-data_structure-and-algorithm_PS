# 전화번호 목록

def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1) :
        mini = min(len(phone_book[i]), len(phone_book[i+1]))
        if phone_book[i][:mini]==phone_book[i+1][:mini] :
            return False

    return True

books = ["123","456","789"]
print(solution(books))



