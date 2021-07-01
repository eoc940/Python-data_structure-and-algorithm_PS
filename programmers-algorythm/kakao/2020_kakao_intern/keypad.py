# 키패드 누르기

def left_location(val, keypad):
    for i in range(2):
        for j in range(4):
            if val==keypad[j][i]:
                return (j,i)

def right_location(val, keypad):
    for i in range(2,0,-1):
        for j in range(4):
            if val==keypad[j][i]:
                return (j,i)

def center_location(val, keypad):
    for i in range(4):
        if val==keypad[i][1]:
            return (i,1)

def solution(numbers, hand):
    answer = ''
    keypad = [[1,2,3],[4,5,6],[7,8,9],["*",0,"#"]]
    left, right = (3,0),(3,2)
    for x in numbers:
        if x in [1,4,7,"*"]:
            left = left_location(x, keypad)
            answer += "L"

        elif x in [3,6,9,"#"]:
            right = right_location(x, keypad)
            answer += "R"
        else :
            location = center_location(x, keypad)
            # print(location)
            # print(left, right)
            left_dist = abs(left[0]-location[0]) + abs(left[1]-location[1])
            right_dist = abs(right[0]-location[0]) + abs(right[1]-location[1])
            if left_dist > right_dist:
                right = location
                answer += "R"
            elif left_dist < right_dist:
                left = location
                answer += "L"
            else :
                if hand=="right":
                    right = location
                    answer += "R"
                else :
                    left = location
                    answer += "L"

    return answer

numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"
print(solution(numbers, hand))