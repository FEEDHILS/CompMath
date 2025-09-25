import numpy as np
import matplotlib.pyplot as plt

# [Основные Настройки]
func = lambda x: (x**2 - np.sin(x))
steps = 11
start = 0.5
end = 1
testPoint = 0.77 # 0.77, 0.52, 0.97, 0.73 - из таблицы 1


space = np.linspace(start, end, 200) # Качество рисования Оригинала и Интерполяции
stepIter = (end - start) / (steps - 1) # Длина шага
pointsX = [start + i*stepIter for i in range(steps)]
pointsY = [func(i) for i in pointsX]

region = lambda x: min(steps-2, int( (x - start) / stepIter )) # Вспомогательная формула для нахождения области точки.