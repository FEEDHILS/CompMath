from utils import *


# Интерполяция Лагранжом первого порядка
L1 = lambda x: pointsY[region(x)] * (x - pointsX[region(x)+1]) / (pointsX[region(x)] - pointsX[region(x)+1]) \
                    + pointsY[region(x)+1] * (x - pointsX[region(x)]) / (pointsX[region(x)+1] - pointsX[region(x)])



# Оценка Погрешности по остаточному члену Лагранжа:

# (x^2 - sin(x))'' = 2 + sin(x) - Данная функция имеет область значений [1; 3]
# Множитель остаточного члена, w2(x) имеет мин = 0 (в точках на границах области), и макс = h^2, где h - длина области.
# Поскольку обе скобки в w2 имеют своим максимумом h (если точка на противоположном краю), то w2 не превышает h*h = h^2
minR = 0
maxR = (3*stepIter**2)/2
R = lambda x: abs( L1(x) - func(x) )

if __name__ == "__main__":
    print("[Интерполяция Лагранжа первого порядка]")

    print("Проверка неравенства minR < R(x*) < maxR: ", minR < R(testPoint) < maxR)
    print(f"Погрешность <= 10^-4? ", R(testPoint) <= 10**(-4) )
    print()
    
    print("[R(x*), L1(x*), f(x*)]")
    print(R(testPoint), L1(testPoint), func(testPoint), sep=", ")