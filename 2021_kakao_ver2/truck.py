
MAX_BIKE = 20

'''
0: 6초간 아무것도 하지 않음
1: 위로 한 칸 이동
2: 오른쪽으로 한 칸 이동
3: 아래로 한 칸 이동
4: 왼쪽으로 한 칸 이동
5: 자전거 상차
6: 자전거 하차
'''

class truck:
    tid:int = 0
    lid:int = 0
    bike:int = 0
    command:list = []
    length:int = 0

    def __init__(self, tid, lid, bike, command, MAX_LENG):
        self.tid = tid
        self.lid = lid
        self.bike = bike
        self.command = command
        self.length = MAX_LENG

    def up(self):
        if self.lid % self.length < self.length-1:
            self.lid += 1
            self.command.append(1)
    def down(self):
        if self.lid % self.length > 0:
            self.lid -= 1
            self.command.append(3)
    def right(self):
        if self.lid < self.length**2 - self.length:
            self.lid += self.length
            self.command.append(2)
    def left(self):
        if self.lid >= self.length:
            self.lid -= self.length
            self.command.append(4)
    def load(self):
        if self.bike < MAX_BIKE:
            self.bike += 1
            self.command.append(5)
    def land(self):
        if self.bike > 0:
            self.bike -= 1
            self.command.append(6)

