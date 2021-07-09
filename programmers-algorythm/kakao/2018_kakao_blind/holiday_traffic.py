# 추석 트래픽

def solution(lines):
    answer = 0
    times = []
    for line in lines:
        time = 0
        info = line.split(" ")
        clock, minute, second = info[1].split(":")

        time += 60*60 * int(clock)
        time += 60 * int(minute)
        time += float(second)
        start = round(time - float(info[2][:-1]) + 1/1000,3)
        end = time
        # print(float(info[2][:-1]),start, end)
        times.append((start, end))
    times.sort(key=lambda x : x[0])
    print(times)
    point = []
    for x1, x2 in times:
        point.append(x1)
        point.append(x2)
    point.sort()
    print(point)
    for time_st in point:
        time_en = round(time_st + 0.999,3)
        print(time_en)
        cnt = 0
        for log_st, log_en in times:
            if time_st<=log_st<=time_en or time_st<=log_en<=time_en or time_st>=log_st and time_en<=log_en:
                cnt += 1
        answer = max(answer, cnt)

    return answer

_input = [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]

_input = ["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]

print(solution(_input))

