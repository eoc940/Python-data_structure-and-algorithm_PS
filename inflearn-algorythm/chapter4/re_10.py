# 증가수열 만들기(그리디)

import sys

n= int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

left = 0
right = len(nums)-1
cnt = 0
letter = ""
last = 0


while left < right :

    if nums[left] > last and nums[right] > last :
        cnt += 1
        if nums[left] > nums[right] :
            last = nums[right]
            right -= 1
            letter += "R"
        else :
            last = nums[left]
            left += 1
            letter += "L"
    elif nums[left] > last and nums[right] < last :
        cnt += 1
        last = nums[left]
        left += 1
        letter += "L"
    elif nums[left] < last and nums[right] > last:
        cnt += 1
        last = nums[right]
        right -= 1
        letter += "R"
    else :
        break

print(cnt)
print(letter)