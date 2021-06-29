# 베스트 앨범

from collections import defaultdict
import operator

def solution(genres, plays):
    answer = []
    order = defaultdict(int)
    song = defaultdict(list)
    for i in range(len(genres)):
        order[genres[i]] += plays[i]
        song[genres[i]].append([i, plays[i]])
    # print(order)
    # print(song)
    ordered = sorted(order.items(), key=operator.itemgetter(1), reverse=True)
    # print(ordered)
    for gen, total in ordered:
        for i in range(2):
            song_li = sorted(song[gen], key=lambda x : x[1], reverse=True)
            # print(song_li)
            try :
                answer.append(song_li[i][0])
            except:
                break
    return answer

genres = ["classic", "pop", "classic", "classic", "pop","jazz"]
plays = [500, 600, 150, 800, 2500,6000]
print(solution(genres, plays))
