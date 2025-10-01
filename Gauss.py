from utils import *
from math import factorial as fact


def GaussForward(x):
    result = pointsY[0]
    before = 1
    
    t = (x - pointsX[0])/stepIter # if x = x_0 + th
    for i in range(1, steps):
        before *= (t - (i-1))
        result += FiniteDiff(i) * before / fact(i)

    return result

