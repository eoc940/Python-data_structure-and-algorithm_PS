# 광고 삽입

def conv_sec(time):
    time_list = time.split(":")
    return int(time_list[0])*60*60 + int(time_list[1])*60 + int(time_list[2])

def solution(play_time, adv_time, logs):

    total_time = conv_sec(play_time)
    time_list = [0]*(total_time+1)
    for log in logs:
        start, end = log.split("-")
        start = conv_sec(start)
        end = conv_sec(end)
        time_list[start] += 1
        time_list[end] -= 1
    for i in range(1, total_time+1):
        time_list[i] += time_list[i-1]

    adv_total = conv_sec(adv_time)
    _sum = sum(time_list[:adv_total])
    # 첫 초기화를 반드시 해주자!!
    max_sum = _sum
    max_idx = 0
    for i in range(total_time-adv_total):
        _sum -= time_list[i]
        _sum += time_list[adv_total + i]
        if _sum > max_sum:
            max_sum = _sum
            max_idx = i+1

    hour = max_idx//3600
    max_idx -= hour*3600
    minute = max_idx//60
    max_idx -= minute*60
    second = max_idx

    return str(hour).zfill(2) + ":" + str(minute).zfill(2) + ":" + str(second).zfill(2)

play_time = "99:59:59"
adv_time = "25:00:00"
logs = ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
print(solution(play_time, adv_time, logs))