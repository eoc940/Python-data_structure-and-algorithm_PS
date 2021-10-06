# 베스트 앨범

from collections import defaultdict

def solution(genres, plays):
    answer = []
    songs = defaultdict(list)
    play_time = defaultdict(int)
    for i, (genre, play) in enumerate(zip(genres, plays)):
        songs[genre].append((i, play))
        play_time[genre] += play

    # print(songs)
    # print(play_time)
    genre_play_time = []
    for key, val in play_time.items():
        genre_play_time.append((key, val))

    genre_play_time.sort(key = lambda x : x[1], reverse=True)

    for genr, time in genre_play_time:
        song_list = songs[genr]
        song_list.sort(key=lambda x : x[1], reverse=True)
        # print(song_list)
        if len(song_list) >= 2:
            for i in range(2):
                answer.append(song_list[i][0])
        else:
            answer.append(song_list[0][0])

    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))