from utils import *

# Интерполяция Ньютоном второго порядка
PointDeriv = [ (pointsY[i+1]-pointsY[i])/(stepIter) for i in range(steps-1)]


def N2(x):
    a = min(region(x), steps-3) # x_i-1
    b = min(region(x) + 1, steps-2) # x_i
    c = min(region(x) + 2, steps-1) # x_i+1    
    SecondDeriv = (PointDeriv[b]-PointDeriv[a])/(2*stepIter)

    return pointsY[a] + PointDeriv[a] * (x - pointsX[a]) \
        + SecondDeriv * (x - pointsX[a]) * (x - pointsX[b])

R = lambda x: abs( N2(x) - func(x) )