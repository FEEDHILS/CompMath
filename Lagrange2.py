from utils import *

# Интерполяция Лагранжом второго порядка
def L2(x):
    first = min(region(x), steps-3) # x_i-1
    second = min(region(x) + 1, steps-2) # x_i
    third = min(region(x) + 2, steps-1) # x_i+1

    return pointsY[first] * (x - pointsX[second])*(x - pointsX[third]) / ((pointsX[first] - pointsX[second])*(pointsX[first] - pointsX[third])) \
        + pointsY[second] * (x - pointsX[first])*(x - pointsX[third]) / ((pointsX[second] - pointsX[first])*(pointsX[second] - pointsX[third])) \
        + pointsY[third] * (x - pointsX[first])*(x - pointsX[second]) / ((pointsX[third] - pointsX[first])*(pointsX[third] - pointsX[second]))



# Оценка Погрешности по остаточному члену Лагранжа:

# (x^2 - sin(x))''' = cos(x) - Данная функция имеет область значений [-1; 1]
# Множитель остаточного члена, w3(x) имеет мин = 0 (в точках на границах области), и макс = 4h^3, где h - длина области.
# Поскольку первая и посл. скобки в w3 имеют своим максимумом 2h (если точка на противоположном краю),
# А скобка посередине имеет своим максимумом h (если точка на краях области).
minR = 0
maxR = 4*(stepIter**3)/6
R = lambda x: abs( L2(x) - func(x) )

if __name__ == "__main__":
    print("[Интерполяция Лагранжа второго порядка]")

    print("Проверка неравенства minR < R(x*) < maxR: ", minR < R(testPoint) < maxR)
    print(f"Погрешность <= 10^-5? ", R(testPoint) <= 10**(-5) )
    print()

    print("[R(x*), L2(x*), f(x*)]")
    print(R(testPoint), L2(testPoint), func(testPoint), sep=", ")