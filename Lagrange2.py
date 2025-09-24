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




# Интерполяция Лагранжом второго порядка
def L2(x):
    first = min(region(x), steps-3) # x_i-1
    second = min(region(x) + 1, steps-2) # x_i
    third = min(region(x) + 2, steps-1) # x_i+1

    return pointsY[first] * (x - pointsX[second])*(x - pointsX[third]) / ((pointsX[first] - pointsX[second])*(pointsX[first] - pointsX[third])) \
        + pointsY[second] * (x - pointsX[first])*(x - pointsX[third]) / ((pointsX[second] - pointsX[first])*(pointsX[second] - pointsX[third])) \
        + pointsY[third] * (x - pointsX[first])*(x - pointsX[second]) / ((pointsX[third] - pointsX[first])*(pointsX[third] - pointsX[second]))



plt.plot(space, [L2(i) for i in np.linspace(start, end, 200)], c="blue",)



# Погрешность 

# Оценка Погрешности по остаточному члену Лагранжа:

# (x^2 - sin(x))''' = cos(x) - Данная функция имеет область значений [-1; 1]
# Множитель остаточного члена, w3(x) имеет мин = 0 (в точках на границах области), и макс = 4h^3, где h - длина области.
# Поскольку первая и посл. скобки в w3 имеют своим максимумом 2h (если точка на противоположном краю),
# А скобка посередине имеет своим максимумом h (если точка на краях области).

testPoint = 0.77 # 0.77, 0.52, 0.97, 0.73 - из таблицы 1

minR = 0
maxR = 4*(stepIter**3)/6
R = lambda x: abs( L2(x) - func(x) )

print("[Проверка Погрешности в x*]")
print("Проверка неравенства minR < R < maxR: ", minR < R(testPoint) < maxR)
print(f"Погрешность <= 10^-5? ", R(testPoint) <= 10**(-5) )
print()

print("[R(x*), L2(x*), f(x*)]")
print(R(testPoint), L2(testPoint), func(testPoint), sep=", ")

plt.show()