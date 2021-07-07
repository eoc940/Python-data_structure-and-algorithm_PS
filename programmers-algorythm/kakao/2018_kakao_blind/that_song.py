# 방금 그곡

def play_time_cal(start, end):
    st_hour, st_min = start.split(":")
    en_hour, en_min = end.split(":")
    return 60*(int(en_hour)-int(st_hour)) + int(en_min) - int(st_min)

def convert(m):
    m = m.replace("C#", "c")
    m = m.replace("A#", "a")
    m = m.replace("D#", "d")
    m = m.replace("F#", "f")
    m = m.replace("G#", "g")
    return m

def solution(m, musicinfos):
    m = convert(m)
    answer = []
    result = '';
    for info in musicinfos:
        start, end, song, melody = info.split(",")
        melody = convert(melody)

        played = "";
        play_time = play_time_cal(start, end)
        for i in range(play_time):
            played += melody[i%len(melody)]
        print(m, melody,played)
        if m in played:
            answer.append((play_time, start, song))
    # print(answer,"!!")
    if len(answer) == 1:
        result = answer[0][2]
    elif not answer :
        result = "(None)"
    elif len(answer) > 1: # 여기가 문제같다
        max_playtime = float('-inf')
        for play_time, start, song in answer :
            if play_time > max_playtime:
                max_playtime = play_time
        answer.sort(key=lambda x: x[1])

        for play_time, start, song in answer :
            if play_time == max_playtime:
                result = song
                break
    # print(answer)
    return result

m = "ABCGG"
musicinfos = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
print(solution(m, musicinfos))

