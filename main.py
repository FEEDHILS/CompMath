from utils import *
from Lagrange1 import L1
from Lagrange2 import L2
from Newton1 import N1
from Newton2 import N2


# [График Оригинала]
plt.figure(1)
plt.plot(space, [func(i) for i in space], c="red", linestyle="dashed",)



# [Точки]
plt.figure(2)
plt.scatter(pointsX, pointsY, marker="*", c="black")



# [График Интерполяции]
interpolation = L1
plt.plot(space, [interpolation(i) for i in space], c="blue",)


plt.show()