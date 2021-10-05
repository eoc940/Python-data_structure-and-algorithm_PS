# 전화번호 목록

def solution(phone_book):

    phone_book.sort()

    for i in range(len(phone_book)-1):
        min_len = min(len(phone_book[i]), len(phone_book[i+1]))
        if phone_book[i][:min_len] == phone_book[i+1][:min_len]:
            return False
    return True

phone_book = ["119", "97674223", "1195524421"]
print(solution(phone_book))