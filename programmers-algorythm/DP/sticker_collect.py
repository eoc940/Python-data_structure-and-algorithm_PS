# 스티커 모으기 2

def solution(sticker):
    answer = 0
    if len(sticker) <= 2:
        return max(sticker)

    # 처음걸 골랐을때
    dp = [0 for _ in range(len(sticker))]
    dp[0] = sticker[0]
    dp[1] = sticker[1]
    dp[2] = max(sticker[0]+sticker[2], sticker[1])
    for i in range(3, len(sticker)):
        dp[i] = max(dp[i-3]+sticker[i],dp[i-2]+sticker[i], dp[i-1])
    dp[-1] = 0
    candi_one = max(dp)

    # 처음걸 안골랐을때
    dp = [0 for _ in range(len(sticker))]
    dp[1] = sticker[1]
    dp[2] = max(sticker[1], sticker[2])
    for i in range(3, len(sticker)):
        dp[i] = max(dp[i-3]+sticker[i],dp[i-2]+sticker[i], dp[i-1])
    candi_two = max(dp)
    # print(candi_one, candi_two)

    return max(candi_one, candi_two)

sticker = [14, 6, 5, 2, 16, 9, 2, 10]
print(solution(sticker))