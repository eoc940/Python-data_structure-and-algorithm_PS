
import math
import sys

xa, ya, xb, yb, xc, yc = map(int, sys.stdin.readline().split())
answer = []
def circular(x1,y1,x2,y2,x3,y3):
    total = 0
    first = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    total += first * 2
    second = math.sqrt((x2-x3)**2 + (y2-y3)**2)
    total += second * 2
    return total

def is_oneline(x1,y1,x2,y2,x3,y3):
    if x2 != x1 and x3 != x2 and (y2-y1)/(x2-x1) == (y3-y2)/(x3-x2):
        return True
    if x1 == x2 and x2 == x3:
        return True
    return False

def process(xa,ya,xb,yb,xc,yc):

    if is_oneline(xa,ya,xb,yb,xc,yc):
        return -1.0

    # 첫번째 점
    x_mid_double = xa + xb
    y_mid_double = ya + yb

    x_point = x_mid_double - xc
    y_point = y_mid_double - yc
    answer.append(circular(xa, ya, xc, yc, xb, yb))

    # 두번째 점
    x_mid_double = xb + xc
    y_mid_double = yb + yc

    x_point = x_mid_double - xa
    y_point = y_mid_double - ya
    answer.append(circular(xb, yb, xa, ya, xc, yc))

    # 세번째 점
    x_mid_double = xc + xa
    y_mid_double = yc + ya

    x_point = x_mid_double - xb
    y_point = y_mid_double - yb
    answer.append(circular(xc, yc, xb, yb, xa, ya))
    # print(answer)
    return max(answer)-min(answer)

print(process(xa,ya,xb,yb,xc,yc))
