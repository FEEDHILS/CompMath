from utils import testPoint as test
from Lagrange1 import R as R1
from Lagrange2 import R as R2
from Newton1 import R as R3
from Newton2 import R as R4


Deviations = [("Lin. Lagrange", R1(test)), ("Quad. Lagrange", R2(test)), ("Lin. Newton", R3(test)), ("Quad. Newton", R4(test))]

Deviations = sorted(Deviations, key=lambda x: x[1])
print(f"Наименьшая погрешность: {Deviations[0][1]}, {Deviations[0][0]}")
print(f"Наибольшая погрешность погрешность: {Deviations[-1][1]}, {Deviations[-1][0]}")

print("[Таблица Погрешностей]")
for i in Deviations:
    print(f"{i[0]} - {i[1]},")