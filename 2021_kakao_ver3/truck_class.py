
# 10으로 돌려보겠다
MAX_BIKE = 10

class truck:
    tid:int = None
    row:int = None
    col:int = None
    lid:int = None
    bike:int = None
    map_leng:int = None

    def __init__(self, tid, lid, bike, map_leng):
        self.tid = tid
        self.lid = lid
        self.bike = bike
        self.map_leng = map_leng
        self.convert()

    def convert(self):
        x,y = divmod(self.lid, self.map_leng)
        self.row = 4-y
        self.col = x

    def up(self):
        if self.row > 0:
            self.row -= 1
            return 1

    def right(self):
        if self.col < self.map_leng - 1:
            self.col += 1
            return 2

    def down(self):
        if self.row < self.map_leng - 1:
            self.row += 1
            return 3

    def left(self):
        if self.col > 0:
            self.col -= 1
            return 4

    def load(self):
        if self.bike < MAX_BIKE:
            self.bike += 1
            return 5

    def land(self):
        if self.bike > 0:
            self.bike -= 1
            return 6

