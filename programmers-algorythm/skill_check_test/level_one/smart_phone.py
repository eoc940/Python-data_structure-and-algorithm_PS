# 스마트폰

def search_location(value):
    location = [[1,2,3],[4,5,6],[7,8,9],["*",0,"#"]]
    for i in range(4):
        for j in range(3):
            if value == location[i][j]:
                return (i,j)

def solution(numbers, hand):
    answer = ''
    left_nums = [1,4,7]
    right_nums = [3,6,9]
    mid_nums = [2,5,8,0]
    left_loca, right_loca = (3,0),(3,2)
    for num in numbers:
        print(left_loca, right_loca, num, answer)
        if num in left_nums:
            left_loca = search_location(num)
            answer += "L"
        elif num in right_nums:
            right_loca = search_location(num)
            answer += "R"
        else: #거리 계산해야함
            x,y = search_location(num)
            left = abs(x-left_loca[0]) + abs(y-left_loca[1])
            right = abs(x-right_loca[0]) + abs(y-right_loca[1])

            if left > right :
                right_loca = (x,y)
                answer += "R"
            elif right > left:
                left_loca = (x,y)
                answer += "L"
            elif right==left:

                if hand=="right":
                    right_loca = (x,y)
                    answer += "R"
                else:
                    left_loca = (x,y)
                    answer += "L"



    return answer

numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"
print(solution(numbers, hand))