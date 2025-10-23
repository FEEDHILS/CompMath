from utils import *
import sympy as sp
from Newton import *
from Gauss import *
from Lagrange import *

print(pointsX, pointsY)
fig, axs = plt.subplots(1, 2, figsize=(14, 5))


axs[0].scatter(pointsX, pointsY, c="black", zorder=5)
axs[0].plot(pointsX, pointsY, c="green", linestyle="dashed")
axs[0].set_title('Таблично заданная функция (какая-то линия)')

expr = LagrangeSym() # Интерполяция Лагранжа в символьном виде
diff1 = sp.diff(expr) # Первая производная
diff2 = sp.diff(diff1) # Вторая производная

axs[1].scatter(pointsX, pointsY, c="black", zorder=5)
axs[1].plot(space, [expr.subs(x, i) for i in space],)
axs[1].set_title('Интерполяция Лагранжа')


R1 = 0
R2 = 0

plt.show()