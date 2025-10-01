import numpy as np
import matplotlib.pyplot as plt

# [Основные Настройки]
func = lambda x: (x**2 - np.sin(x))
steps = 32
start = .5
end = 1


space = np.linspace(start, end, 200) # Качество рисования Оригинала и Интерполяции
stepIter = (end - start) / (steps - 1) # Длина шага
pointsX = [start + i*stepIter for i in range(steps)]
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

FDTable = { (1, i): pointsY[i+1]-pointsY[i] for i in range(steps-1) } # Таблица конечных разностей (Восходящие)
def FiniteDiff(deg, start=0):
    if deg <= 1:
        return FDTable[(deg, start)]
    
    if (deg, start) in FDTable:
        return FDTable[(deg, start)]
    
    result = FiniteDiff(deg-1, start+1) - FiniteDiff(deg-1, start)

    FDTable[(deg, start)] = result
    return result