import numpy as np

# start - начало отрезка
# end - конец отрезка
# points - количество точек(узлов)
# original - подинтегральная функция (для просчета значений в узлах)


def CentralRect(start, end, num, original):
    num += 1
    xRangeLeft = np.linspace(start, end, num)
    xRange = (xRangeLeft[:-1] + xRangeLeft[1:]) / 2 
    y = original(xRange)

    ApproxSum = 0
    for i in range(num-1):
        h = xRangeLeft[1] - xRangeLeft[0]
        ApproxSum += h * y[i]

    return ApproxSum

def Trapezoid(start, end, num, original):
    num += 1
    xRange = np.linspace(start, end, num)
    y = original(xRange)

    ApproxSum = 0
    for i in range(num-1):
        h = xRange[i+1] - xRange[i]
        ApproxSum += h * (y[i] + y[i+1]) / 2

    return ApproxSum

def Simpson(start, end, parabols, original):
    xRange = np.linspace(start, end, 1 + 2*parabols)
    y = original(xRange)

    ApproxSum = 0
    for i in range(0, len(xRange)-2, 2):
        h = xRange[i+1] - xRange[i]
        ApproxSum += h/3 * (y[i] + 4*y[i+1] + y[i+2])

    return ApproxSum

def Weddle(start, end, n, original):
    xRange = np.linspace(start, end, 1 + 6*n)
    y = original(xRange)

    ApproxSum = 0
    for i in range(0, len(xRange)-6, 6):
        h = xRange[i+1] - xRange[i]
        ApproxSum += 0.3 * h * (y[i] + 5*y[i+1] + y[i+2] + 6*y[i+3] + y[i+4] + 5*y[i+5] + y[i+6])

    return ApproxSum