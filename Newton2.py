import numpy as np
import matplotlib.pyplot as plt

# Всякие настройки
func = lambda x: (x**2 - np.sin(x)) # Оригинальная ф-я
steps = 11 # Количество шагов
start = 0.5
end = 1

space = np.linspace(start, end, 200) # Используется при рисовании Оригинала и Интерполяции

stepIter = (end - start) / (steps - 1) # Длина шага
pointsX = [start + i*stepIter for i in range(steps)]
pointsY = [func(i) for i in pointsX]

region = lambda x: min(steps-2, int( (x - start) / stepIter )) # Формула для нахождения !!начала кусочка!! в которой лежит переменная


# График Оригинала
plt.figure(1)
plt.plot(space, [func(i) for i in space], c="red", linestyle="dashed",)



# Точки + график интерполяции
plt.figure(2)
plt.scatter(pointsX, pointsY, marker="*", c="black")




# Интерполяция Ньютоном первого порядка
PointDeriv = [ (pointsY[i+1]-pointsY[i])/(stepIter) for i in range(steps-1)]


def N2(x):
    a = min(region(x), steps-3) # x_i-1
    b = min(region(x) + 1, steps-2) # x_i
    c = min(region(x) + 2, steps-1) # x_i+1    

    return pointsY[a] + PointDeriv[a] * (x - pointsX[a]) \
        + (PointDeriv[b]-PointDeriv[a])/(2*stepIter) * (x - pointsX[a]) * (x - pointsX[b])


plt.plot(space, [N2(i) for i in space], c="blue")

plt.show()