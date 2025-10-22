from utils import *

from Newton import *
from Gauss import *


# [График Оригинала]
plt.figure(1)
plt.plot(space, [func(i) for i in space], c="green", linestyle="dashed",)
plt.title("График функции: x^2 - sin(x)")

fig, axs = plt.subplots(1, 3, figsize=(14, 5))

# [Точки]
a = 0.52
b = 0.97
c = 0.73

axs[0].scatter(pointsX, pointsY, marker="*", c="black")
axs[1].scatter(pointsX, pointsY, marker="*", c="black")
axs[2].scatter(pointsX, pointsY, marker="*", c="black")

# [График Интерполяции]
axs[0].plot(space, [NewtonForward(i) for i in space], c="blue",)
axs[0].scatter(a, NewtonForward(a), marker='o', c='red')

axs[1].plot(space, [NewtonBackward(i) for i in space], c="red",)
axs[1].scatter(b, NewtonBackward(b), marker='o', c='blue')

axs[2].plot(space, [GaussBackward(i) for i in space], c="green",)
axs[2].scatter(c, NewtonForward(c), marker='o', c='red')



axs[0].set_title('Интерполяция Ньютона (Вперед)')
axs[1].set_title('Интерполяция Ньютона (Назад)')
axs[2].set_title('Интерполяция Гаусса (Назад)')


print( "1) Точка x1 - 0.52, Ньютон(Вперед)", NewtonForward(a) )
print( "2) Точка x2 - 0.97, Ньютон(Вперед)", NewtonBackward(b) )
print( "3) Точка x3 - 0.73, Ньютон(Вперед)", GaussBackward(c), "\n" )

# Подсчет погрешности
# Производная моей функции прыгает между sin и cos x. На моем отрезке [0.5, 1]
# В зависимости от четности производной (т.е четности точек) я беру либо sin (1) (тк возр. на отрезке)
# Либо cos(0.5) (тк убыв. на отрезке)
# Это для максимумов. Мин. погрешность, понятное дело = 0

if points % 2 == 0:
    Rmax = (np.sin(1) * (steps * stepIter)**points) / math.factorial(points)
else:
    Rmax = (np.cos(0.5) * (steps * stepIter)**points) / math.factorial(points) 

print("Макс. погрешность -", Rmax)
print( "Проверка для 1)", abs( NewtonForward(a) - func(a) ) < Rmax )
print( "Проверка для 2)", abs( NewtonBackward(b) - func(b) ) < Rmax )
print( "Проверка для 3)", abs( GaussBackward(c) - func(c) ) < Rmax )

plt.show()