'''
0: 6초간 아무것도 하지 않음
1: 위로 한 칸 이동
2: 오른쪽으로 한 칸 이동
3: 아래로 한 칸 이동
4: 왼쪽으로 한 칸 이동
5: 자전거 상차
6: 자전거 하차
'''
# 트럭의 최대 자전거를 2로 제한
MAX_BIKE = 2

class truck:
    tid:int = None
    row:int = None
    col:int = None
    lid:int = None
    bike:int = None
    map_leng:int = None
    command:list = None

    def __init__(self, tid, lid, bike, map_leng, command):
        self.tid = tid
        self.lid = lid
        self.bike = bike
        self.map_leng = map_leng
        self.command = command
        self.convert()

    def convert(self):
        x,y = divmod(self.lid, self.map_leng)
        self.row = 4-y
        self.col = x

    def up(self):
        if self.row > 0:
            self.row -= 1
            self.command.append(1)

    def right(self):
        if self.col < self.map_leng - 1:
            self.col += 1
            self.command.append(2)

    def down(self):
        if self.row < self.map_leng - 1:
            self.row += 1
            self.command.append(3)

    def left(self):
        if self.col > 0:
            self.col -= 1
            self.command.append(4)

    def load(self):
        if self.bike < MAX_BIKE:
            self.bike += 1
            self.command.append(5)

    def land(self):
        if self.bike > 0:
            self.bike -= 1
            self.command.append(6)

