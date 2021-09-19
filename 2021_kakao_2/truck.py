import requests
import json

MAX_COMMAND = 10
MAX_LENG = 5
MIN_ROW, MIN_COL, MAX_ROW, MAX_COL = 0,0,4,4
MIN_BIKE, MAX_BIKE, MAX_LOAD_BIKE = 0,4,20

class truck:
    id:int = None
    bike:int = 0
    row: int = 0
    col: int = 0
    com = []

    def __init__(self, truck_id, bike, row, col,com):
        self.bike = bike
        self.id = truck_id
        self.row = row
        self.col = col
        self.com = com

    def up(self):
        if self.row > MIN_ROW:
            self.row -= 1
            self.com.append(1)
    def down(self):
        if self.row < MAX_ROW:
            self.row += 1
            self.com.append(3)
    def right(self):
        if self.col < MAX_COL:
            self.col += 1
            self.com.append(2)
    def left(self):
        if self.col > MIN_COL:
            self.col -= 1
            self.com.append(4)
    def load(self):
        if locations[self.row][self.col] > MAX_BIKE and self.bike < MAX_LOAD_BIKE:
            locations[self.row][self.col] -=1
            self.bike += 1
            self.com.append(5)
    def land(self):
        if locations[self.row][self.col] < MAX_BIKE and self.bike > MIN_BIKE:
            locations[self.row][self.col] += 1
            self.bike -= 1
            self.com.append(6)

x_auth_token = 'a41a8c80391a691a9bebed17ebd45b56'
url = 'https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users'


def location_mapping(location_id):
    m,n = divmod(location_id, MAX_LENG)
    col = m
    row = 4-n
    return row, col


def startAPI():
    headers = {
        'X-Auth-Token':x_auth_token,
        'Content-Type':'application/json'
    }
    data = '{"problem" : 1}'

    response = requests.post(url+'/start', headers=headers, data=data)
    auth_data = response.json()
    # print(auth_data)
    print(auth_data["auth_key"])
    return auth_data.get("auth_key")

def locationsAPI(auth_key):
    headers = {
        'Authorization':auth_key,
        'Content-Type':'application/json'
    }
    response = requests.get(url+'/locations', headers=headers)
    location = response.json()
    locations = [[0] * MAX_LENG for _ in range(MAX_LENG)]
    for loc in location.get("locations"):
        loca_id = loc["id"]
        bike_count = loc["located_bikes_count"]
        row, col = location_mapping(loca_id)
        locations[row][col] = bike_count
    return locations

def trucksAPI(auth_key):
    headers = {
        'Authorization': auth_key,
        'Content-Type': 'application/json'
    }
    response = requests.get(url+'/trucks', headers=headers)
    trucks = response.json()
    truck_list = []
    for tr in trucks.get("trucks"):
        loca_id = tr["location_id"]
        truck_id = tr["id"]
        row, col = location_mapping(loca_id)

        bike = tr["loaded_bikes_count"]
        truck_list.append(truck(truck_id, bike, row, col, []))
    return truck_list

def simulateAPI(auth_key, commands):
    headers = {
        'Authorization': auth_key,
        'Content-Type': 'application/json'
    }
    data = dict()
    data["commands"] = commands
    datas = json.dumps(data)
    # print(str(data), "###")
    response = requests.put(url+'/simulate', headers=headers, data=datas)
    simulate_response = response.json()
    # print(simulate_response)
    return simulate_response["status"]

def scoreAPI(auth_key):
    headers = {
        'Authorization': auth_key,
        'Content-Type': 'application/json'
    }
    response = requests.get(url+'/score', headers=headers)
    score = response.json()
    score_json = json.loads(json.dumps(score))
    return score_json.get("score")

def move(truck, locations):
    right_leng = truck.id - truck.col

    if right_leng >= 0:
        for _ in range(right_leng):
            truck.right()
    else:
        for _ in range(-right_leng):
            truck.left()
    over = []
    under = []
    for i in range(MAX_LENG):
        if locations[i][truck.col] > MAX_BIKE:
            over.append(i)
        elif locations[i][truck.col] < MAX_BIKE:
            under.append(i)

    # 넘친 것만 있을 때
    if len(over) > 0 and len(under) == 0:
        over.sort()
        if truck.row <= over[0]:
            for _ in range(over[-1]-truck.row):
                if truck.row in over:
                    truck.load()
                truck.down()
        elif over[0] < truck.row < over[-1]:
            for _ in range(truck.row-over[0]):
                if truck.row in over:
                    truck.load()
                truck.up()
            for _ in range(over[-1]-truck.row):
                if truck.row in over:
                    truck.load()
                truck.down()
        elif over[-1] < truck.row:
            for _ in range(truck.row - over[-1]):
                if truck.row in over:
                    truck.load()
                truck.up()

    # 부족한 것만 있을 때
    elif len(under) > 0 and len(over) == 0:
        under.sort()
        if truck.row <= under[0]:
            for _ in range(under[-1] - truck.row):
                if truck.row in under:
                    truck.land()
                truck.down()
        elif under[0] < truck.row < under[-1]:
            for _ in range(truck.row - under[0]):
                if truck.row in under:
                    truck.land()
                truck.up()
            for _ in range(under[-1] - truck.row):
                if truck.row in under:
                    truck.land()
                truck.down()
        elif under[-1] < truck.row:
            for _ in range(truck.row - under[-1]):
                if truck.row in under:
                    truck.land()
                truck.up()

    # 부족한 것, 넘은 거 둘다 있을 때
    elif len(under) > 0 and len(over) > 0:
        under.sort()
        over.sort()
        lower_cnt, higher_cnt = 0,0
        for ov in over:
            if truck.row < ov:
                higher_cnt += 1
            else:
                lower_cnt += 1
        if lower_cnt >= higher_cnt:
            for _ in range(truck.row):
                if truck.row in over:
                    truck.load()
                if truck.row in under:
                    truck.land()
                truck.up()
            for _ in range(MAX_LENG-1):
                if truck.row in over:
                    truck.load()
                if truck.row in under:
                    truck.land()
                truck.down()
        else:
            for _ in range(truck.row):
                if truck.row in over:
                    truck.load()
                if truck.row in under:
                    truck.land()
                truck.down()
            for _ in range(MAX_LENG-1):
                if truck.row in over:
                    truck.load()
                if truck.row in under:
                    truck.land()
                truck.up()
    return truck.com[:MAX_COMMAND]

auth_key = startAPI()

while True:
    locations = locationsAPI(auth_key)
    trucks = trucksAPI(auth_key)

    commands = []

    for i,tr in enumerate(trucks):
        comm = move(tr, locations)
        tmp = dict()
        tmp["truck_id"] = tr.id
        tmp["command"] = comm
        commands.append(tmp)
    for c in commands:
        print(c.get("truck_id"), c.get("command"))
    print()
    if simulateAPI(auth_key, commands) == "finished":
        break

print(scoreAPI(auth_key))



