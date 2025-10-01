from utils import *
from Lagrange1 import L1
from Lagrange2 import L2
from Newton1 import N1
from Newton2 import N2
from Newton import NewtonForward, NewtonBackward


# [График Оригинала]
plt.figure(1)
plt.plot(space, [func(i) for i in space], c="green", linestyle="dashed",)
plt.title("График функции: x^2 - sin(x)")

fig, axs = plt.subplots(1, 2, figsize=(14, 5))

# [Точки]
axs[0].scatter(pointsX, pointsY, marker="*", c="black")
axs[1].scatter(pointsX, pointsY, marker="*", c="black")


# [График Интерполяции]
axs[0].plot(space, [NewtonForward(i) for i in space], c="blue",)
axs[1].plot(space, [NewtonBackward(i) for i in space], c="red",)


axs[0].set_title('Интерполяция Ньютона (Вперед)')
axs[1].set_title('Интерполяция Ньютона (Назад)')


plt.show()