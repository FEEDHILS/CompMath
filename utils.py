import numpy as np
import matplotlib.pyplot as plt
import math

# [Основные Настройки]
func = lambda x: (np.square(x) - np.sin(x)) 
steps = 10
points = steps+1
start = 0.5
end = 1
interRes = points # Разрешение для интерполяторов

space = np.linspace(start, end, 200) # Качество рисования Оригинала и Интерполяции
stepIter = (end - start) / (steps) # Длина шага
pointsX = [start + i*stepIter for i in range(steps+1)]
pointsY = [func(i) for i in pointsX]

# [Вспомогательные функции]
region = lambda x: min(steps-2, int( (x - start) / stepIter )) # Для нахождения области точки.


DDTable = {} # Таблица разделенных разностей
def DividedDiff(x1, x2):
    if abs(x2 - x1) <= 1:
        return (pointsY[x2] - pointsY[x1]) / stepIter
    
    if (x1, x2) in DDTable:
        return DDTable[(x1, x2)]
    
    result = (DividedDiff(x1+1, x2) - DividedDiff(x1, x2-1)) / ( stepIter*(x2 - x1) )
    DDTable[(x1, x2)] = result
    return result



FDTable = { (1, i): pointsY[i+1]-pointsY[i] for i in range(points-1) } # Таблица конечных разностей (Восходящие)
for deg in range(2, points):
    for i in range(points-deg):
        FDTable[(deg, i)] = FDTable[(deg-1, i+1)] - FDTable[(deg-1, i)]

print('Таблица конечных разностей готова! \n')