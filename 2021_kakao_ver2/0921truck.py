import json
import requests
import random
from truck import truck

token = 'd72d58639ce36e6e9e83724eee6a6e89'
url = 'https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users'

# 시나리오 1 기준, 시나리오 2일때는 값을 바꿔준다
MAX_LENG = 5
AVG_BIKE = 4

# API

def startAPI(problem):
    headers = {
        'X-Auth-Token': token,
        'Content-Type': 'application/json'
    }
    data = json.dumps({"problem":problem})
    response = requests.post(url+'/start', headers=headers, data=data)
    auth_result = response.json()
    print(auth_result)
    return auth_result["auth_key"]

def locationAPI(auth_key):
    headers = {
        'Authorization':auth_key,
        'Content-Type': 'application/json'
    }
    response = requests.get(url+'/locations', headers=headers)
    location_result = response.json()
    locations = dict()
    for info in location_result["locations"]:
        locations[info["id"]] = [info["located_bikes_count"], False]
    return locations

def truckAPI(auth_key):
    headers = {
        'Authorization': auth_key,
        'Content-Type': 'application/json'
    }
    response = requests.get(url+'/trucks', headers=headers)
    truck_result = response.json()
    trucks = list()
    for info in truck_result["trucks"]:
        trucks.append(truck(info["id"], info["location_id"], info["loaded_bikes_count"], [], MAX_LENG))

    return trucks

# commands 파라미터는 [{},{}...] 형태로 들어와야 한다
def simulateAPI(auth_key, commands):
    headers = {
        'Authorization': auth_key,
        'Content-Type': 'application/json'
    }
    data = json.dumps({
        "commands":commands
    })
    # print(commands)
    response = requests.put(url + '/simulate', headers=headers, data=data)

    simulate_result = response.json()

    fail_cnt = simulate_result["failed_requests_count"]
    status = simulate_result["status"]
    return fail_cnt, status

def scoreAPI(auth_key):
    headers = {
        'Authorization': auth_key,
        'Content-Type': 'application/json'
    }
    response = requests.get(url+'/score', headers=headers)
    score_result = response.json()
    return score_result["score"]

# function

def distance(location_id, truck):

    x1, y1 = divmod(location_id, MAX_LENG)
    x2, y2 = divmod(truck.lid, MAX_LENG)
    total_dist = abs(x1-x2) + abs(y1-y2)
    return (x1-x2, y1-y2), total_dist


# { "truck_id": 0, "command": [2, 5, 4, 1, 6] }이런 형태 리턴
def move(locations, tr):

    if locations[tr.lid][0] >= AVG_BIKE:
        locations[tr.lid][0] -= 1
        tr.load()
    elif locations[tr.lid][0] < AVG_BIKE-1:
        locations[tr.lid][0] += 1
        tr.land()
    while len(tr.command) < 10:
        direction = random.randrange(1, 5)
        if direction == 1:
            tr.up()
        elif direction == 2:
            tr.down()
        elif direction == 3:
            tr.right()
        elif direction == 4:
            tr.left()
        if locations[tr.lid][0] >= AVG_BIKE:
            locations[tr.lid][0] -= 1
            tr.load()
        elif locations[tr.lid][0] < AVG_BIKE - 1:
            locations[tr.lid][0] += 1
            tr.land()

    return {"truck_id": tr.tid, "command": tr.command[:10]}

# 시나리오 1
auth_key = startAPI(1)
fail_cnt = 0
while True:
    locations = locationAPI(auth_key)
    trucks = truckAPI(auth_key)
    commands = []
    for tr in trucks:
        # command_path는 { "truck_id": 0, "command": [2, 5, 4, 1, 6] }이런 형태
        command_path = move(locations, tr)
        commands.append(command_path)
    fail, status = simulateAPI(auth_key, commands)
    if status == "finished":
        fail_cnt = fail
        break

print(scoreAPI(auth_key))
success = 1428 - int(float(fail_cnt))
print(success, "/", 1428)
print("default success = 1077")

# 시나리오 2
MAX_LENG = 60
AVG_BIKE = 3
auth_key = startAPI(2)
while True:
    locations = locationAPI(auth_key)
    trucks = truckAPI(auth_key)
    commands = []
    for tr in trucks:
        # command_path는 { "truck_id": 0, "command": [2, 5, 4, 1, 6] }이런 형태
        command_path = move(locations, tr)
        commands.append(command_path)

    fail, status = simulateAPI(auth_key, commands)
    if status == "finished":
        fail_cnt = fail
        break

print(scoreAPI(auth_key))
success = 10829 - int(float(fail_cnt))
print(success, "/", 10829)
print("default success = 9142")