from utils import *
from math import factorial as fact


m = interRes

def NewtonForward(x): # If x is between x_0 and x_1
    result = pointsY[0]
    before = 1

    t = (x - pointsX[0])/stepIter # if x = x_0 + th
    for i in range(1, m):
        before *= (t - (i-1))
        result += FDTable[(i,0)] * before / fact(i)

    return result

def NewtonBackward(x):  # If x is between x_n-1 and x_n
    result = pointsY[-1]
    before = 1
    
    t = (x - pointsX[-1])/stepIter
    for i in range(1, m):
        before *= (t + (i-1))
        result += FDTable[(i,points-1-i)] * before / fact(i)

    return result