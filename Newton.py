from utils import *
from math import factorial as fact

def NewtonForward(x): # If x is between x_0 and x_1
    result = pointsY[0]
    before = 1
    
    t = (x - pointsX[0])/stepIter # if x = x_0 + th
    for i in range(1, steps):
        before *= (t - i + 1)
        result += FiniteDiff(i) * before / fact(i)

    return result

def NewtonBackward(x):  # If x is between x_n-1 and x_n
    result = pointsY[-1]
    before = 1
    
    t = (x - pointsX[-1])/stepIter
    for i in range(1, steps):
        before *= (t + i - 1)
        result += FiniteDiff(i, steps - i - 1) * before / fact(i)

    return result