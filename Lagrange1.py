import numpy as np
import matplotlib.pyplot as plt

func = lambda x: (x**2 - np.sin(x))
steps = 11
start = 0.5 # a
end = 1 # b

space = np.linspace(start, end, 200)

stepIter = (end - start) / (steps - 1)
pointsX = [start + i*stepIter for i in range(steps)]
pointsY = [func(i) for i in pointsX]

region = lambda x: min(steps-2, int( (x - start) / stepIter )) # Формула для нахождения кусочка в которой лежит переменная


plt.figure(1)
# Оригинальная функция
plt.plot(space, [func(i) for i in space], c="red", linestyle="dashed",)



plt.figure(2)
# Сетчатая функция
plt.scatter(pointsX, pointsY, marker="x", c="black")

# Интерполяция Лагранжом первого порядка
L1 = lambda x: pointsY[region(x)] * (x - pointsX[region(x)+1]) / (pointsX[region(x)] - pointsX[region(x)+1]) \
                    + pointsY[region(x)+1] * (x - pointsX[region(x)]) / (pointsX[region(x)+1] - pointsX[region(x)])

plt.plot(space, [L1(i) for i in space], c="blue",)



# Погрешность 

# Оценка Погрешности по остаточному члену Лагранжа:

# (x^2 - sin(x))'' = 2 + sin(x) - Данная функция имеет область значений [1; 3]
# Множитель остаточного члена, w2(x) имеет мин = 0 (в точках на границах области), и макс = h^2, где h - длина области.
# Поскольку обе скобки в w2 имеют своим максимумом h (если точка на противоположном краю), то (гипотетический) макс. получится h*h = h^2

testPoint = 0.77 # 0.77, 0.52, 0.97, 0.73 - из таблицы 1

minR = 0
maxR = 3*stepIter # stepIter - длина шага, учитывая что области одного размера, то это длина любой области, т.е h
R = lambda x: L1(x) - func(x)

print("Проверка неравенства minR < R < maxR: ", minR < R(testPoint) < maxR)
print("Погрешность <= 10^-4? ", R(testPoint) <= 10**(-4) )
# print(R(testPoint), L1(testPoint), func(testPoint))

plt.show()