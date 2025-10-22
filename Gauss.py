from utils import *
import math

s = interRes

def GaussBackward(x):
    mid = math.floor( (points)/2 )
    result = pointsY[mid]
    before = 1
    
    t = (x - pointsX[mid])/stepIter
    j = 0
    for i in range(1, s):
        if i%2 != 0:
            mid -= 1
    
        before *= ( t + math.floor(i/2)*(-1)**i )
        result += FDTable[(i, mid)] * before / math.factorial(i)

        if i%2 == 0:
            j += 1

    return result


def GaussForward(x):
    mid = math.floor( (points)/2 )
    result = pointsY[mid]
    before = 1
    
    t = (x - pointsX[mid])/stepIter
    j = 0
    for i in range(1, s):
        if i%2 == 0:
            mid -= 1

        before *= ( t - math.floor(i/2)*(-1)**i )
        result += FDTable[(i, mid)] * before / math.factorial(i)

        if i%2 == 0:
            j += 1
    
    return result

