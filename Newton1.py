from utils import *


# Интерполяция Ньютоном первого порядка
# PointDeriv = [ (pointsY[i+1]-pointsY[i])/(stepIter) for i in range(steps-1)]

N1 = lambda x: pointsY[region(x)] + PointDeriv[region(x)]*(x - pointsX[region(x)])


R = lambda x: abs( N1(x) - func(x) )