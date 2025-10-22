from utils import *
from math import factorial
import sympy as sp

def Lagrange(x):
    result = 0
    for i in range(interRes): # слагаемые
        result2 = 1
        for j in range(interRes): # для слагаемых
            if (i != j):
                result2 *= ( x - pointsX[j] ) / ( stepIter*(i-j) )
        
        result += result2 * pointsY[i]
    
    return result

x,y = sp.symbols('x y')
def LagrangeSym():
    result = 0
    for i in range(interRes): # слагаемые
        result2 = 1
        for j in range(interRes): # для слагаемых
            if (i != j):
                result2 *= ( x - pointsX[j] ) / ( stepIter*(i-j) )
        
        result += result2 * pointsY[i]
    
    return result