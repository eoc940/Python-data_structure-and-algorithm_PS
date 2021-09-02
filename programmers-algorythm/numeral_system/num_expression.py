# 숫자의 표현

def solution(n):
    answer = 0
    nums = [x+1 for x in range(n)]
    num_sum = [0]
    for num in nums:
        num_sum.append(num_sum[-1] + num)
    # print(nums)
    # print(num_sum)

    for i in range(len(num_sum)):
        for j in range(i, len(num_sum)):
            _sum = num_sum[j] - num_sum[i]
            if _sum < n: continue
            elif _sum == n:
                answer += 1
                break
            else: break

    return answer

print(solution(15))