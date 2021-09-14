# 삼각 달팽이

def solution(n):

    nums = [[0]*(x+1) for x in range(n)]
    direct = 0
    row, col = -1,0
    num = 0
    for x in range(n, 0, -1): # 4 3 2 1
        if direct == 0: # 밑으로 내려감
            direct = 1
            for i in range(x):
                num += 1
                row += 1
                nums[row][col] = num

        elif direct == 1: # 옆으로 감
            direct = 2
            for i in range(x):
                num += 1
                col += 1
                nums[row][col] = num

        else: # 위로 올라감
            direct = 0
            for i in range(x):
                num += 1
                col -= 1
                row -= 1
                nums[row][col] = num

    return sum(nums, [])

n = 5
print(solution(n))
