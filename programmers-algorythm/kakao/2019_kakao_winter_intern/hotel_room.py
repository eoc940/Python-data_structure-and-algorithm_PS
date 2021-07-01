# 호텔 방 배정

import sys

sys.setrecursionlimit(10000000)

def find_room(num, rooms) :
    if num not in rooms.keys():
        rooms[num] = num+1
        print(rooms)
        return num
    empty = find_room(rooms[num], rooms)
    rooms[num] = empty+1
    return empty

def solution(k, room_number):
    rooms = dict()
    for num in room_number:
        find_room(num, rooms)
    return list(rooms.keys())

k = 10
room_number = [3,3,3,2,4,4,3]
print(solution(k,room_number))