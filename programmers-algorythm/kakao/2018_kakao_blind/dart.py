# [1차] 다트 게임

def solution(dartResult):
    dartResult = dartResult.replace("10","X")
    # print(dartResult)
    num = 0
    nums = []
    options = []
    for x in dartResult:
        if x.isdigit() :
            num = int(x)
        elif x=="X":
            num = 10
        elif x=="S":
            nums.append(num**1)
            options.append(0)
        elif x=="D":
            nums.append(num**2)
            options.append(0)
        elif x=="T":
            nums.append(num**3)
            options.append(0)
        else:
            options[-1] = x
    # print(nums)
    # print(options)
    for i in range(3):
        if options[i]=="#":
            nums[i] *= -1
        elif options[i]=="*":
            if i==0:
                nums[i] *= 2
            elif i>0:
                nums[i-1] *= 2
                nums[i] *= 2
    # print(nums)
    return sum(nums)

dart = "1T2D3D#"
print(solution(dart))

