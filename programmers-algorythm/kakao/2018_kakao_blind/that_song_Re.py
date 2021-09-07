# 방금그곡

def remove_sharp(m):
    convert = [("C#", "c"), ("D#", "d"),("F#", "f"),("G#", "g"),("A#", "a")]
    for conv in convert:
        m = m.replace(conv[0], conv[1])
    return m

def calculate_time(start, end):
    start = start.split(":")
    end = end.split(":")
    return 60*(int(end[0]) - int(start[0])) + int(end[1]) - int(start[1])

def all_song(time, m):
    song = ''
    for i in range(time):
        song += m[i%len(m)]
    return song

def solution(m, musicinfos):
    answer = []
    m = remove_sharp(m)
    for idx,music in enumerate(musicinfos):
        musicinfos[idx] = remove_sharp(music).split(",")

    for music in musicinfos:
        time = calculate_time(music[0], music[1])
        if m in all_song(time, music[3]):
            answer.append((music[2], time, music[0]))

    if len(answer) == 1: return answer[0][0]
    elif len(answer) == 0: return "(None)"
    else:
        answer.sort(key=lambda x : x[1], reverse=True)
        name, max_time, start_time = answer[0]

        for candi in answer:
            if candi[1] >= max_time:
                if candi[2] < start_time:
                    name = candi[0]
            else: break
        return name

m = "ABC"
musicinfos = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
print(solution(m, musicinfos))

