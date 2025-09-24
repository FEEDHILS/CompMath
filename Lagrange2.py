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


# Оригинальная функция
plt.figure(1)
plt.plot(space, [func(i) for i in space], c="red", linestyle="dashed",)



# Сетчатая функция
plt.figure(2)
plt.scatter(pointsX, pointsY, marker="*", c="black")


# Интерполяция Лагранжом первого порядка
L1 = lambda x: pointsY[region(x)] * (x - pointsX[region(x)+1]) / (pointsX[region(x)] - pointsX[region(x)+1]) \
                    + pointsY[region(x)+1] * (x - pointsX[region(x)]) / (pointsX[region(x)+1] - pointsX[region(x)])


def L2(x):
    first = min(region(x), 8) # x_i-1
    second = min(region(x) + 1, 9) # x_i
    third = min(region(x) + 2, 10) # x_i+1

    return pointsY[first] * (x - pointsX[second])*(x - pointsX[third]) / ((pointsX[first] - pointsX[second])*(pointsX[first] - pointsX[third])) \
        + pointsY[second] * (x - pointsX[first])*(x - pointsX[third]) / ((pointsX[second] - pointsX[first])*(pointsX[second] - pointsX[third])) \
        + pointsY[third] * (x - pointsX[first])*(x - pointsX[second]) / ((pointsX[third] - pointsX[first])*(pointsX[third] - pointsX[second]))


print(pointsX[0])
print(pointsX[2])
plt.plot(space, [L2(i) for i in np.linspace(start, end, 200)], c="blue",)



# Погрешность 

# Оценка Погрешности по остаточному члену Лагранжа:

# (x^2 - sin(x))'' = 2 + sin(x) - Данная функция имеет область значений [1; 3]
# Множитель остаточного члена, w2(x) имеет мин = 0 (в точках на границах области), и макс = h^2, где h - длина области.
# Поскольку обе скобки в w2 имеют своим максимумом h (если точка на противоположном краю), то (гипотетический) макс. получится h*h = h^2

testPoint = 0.77 # 0.77, 0.52, 0.97, 0.73 - из таблицы 1

# minR = 0
# maxR = 3*stepIter
# R = lambda x: abs( L1(x) - func(x) )

# print("Проверка неравенства minR < R < maxR: ", minR < R(testPoint) < maxR)
# print(f"Погрешность <= 10^-4? ", R(testPoint) <= 10**(-4) )
# print(R(testPoint), L1(testPoint), func(testPoint))

plt.show()