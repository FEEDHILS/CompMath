from math import factorial
import sympy as sp

# def Lagrange(x):
#     result = 0
#     for i in range(interRes): # слагаемые
#         result2 = 1
#         for j in range(interRes): # для слагаемых
#             if (i != j):
#                 result2 *= ( x - pointsX[j] ) / ( stepIter*(i-j) )
        
#         result += result2 * pointsY[i]
    
#     return result

x = sp.symbols('x')
def LagrangeSym(points, y, h):
    result = 0
    for i in range(len(points)):
        result2 = 1
        for j in range(len(points)):
            if (i != j):
                result2 *= ( x - points[j] ) / ( h*(i-j) )
        
        result += result2 * y[i]
    
    return result