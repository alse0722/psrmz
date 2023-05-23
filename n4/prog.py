import math
import numpy as np

xx1 = -1
xx2 = 0
eps = 0.000001
alfa = 0.13



def J(x, y):
    r1 = -2*x + y*(math.tan(x*y) ** 2 + 1)
    r2 = x * (math.tan(x*y)**2 + 1)
    r3 = 1.6 * x
    r4 = 4 * y

    m = [[float(r1), float(r2)], [float(r3), float(r4)]]
    print('Jacob:')
    print(m)

    m_inv = np.linalg.inv(m)
    m_inv[0][0] = round(m_inv[0][0], 6)
    m_inv[0][1] = round(m_inv[0][1], 6)
    m_inv[1][0] = round(m_inv[1][0], 6)
    m_inv[1][1] = round(m_inv[1][1], 6)
    print('Jacob inv: ')
    print(m_inv)

    return m_inv


def fun(x, y):
    r1 = math.tan(x*y) - x ** 2
    r2 = 0.8*x*x + 2*y*y - 1
    print('Fun:')
    print([[float(r1)], [float(r2)]])
    return [[float(r1)], [float(r2)]]


def iter(x, y):
    x1 = [[x], [y]]
    x2 = [[x], [y]] - J(x, y).dot(fun(x, y))
    x1[0][0] = round(x1[0][0], 6)
    x1[1][0] = round(x1[1][0], 6)
    x2[0][0] = round(x2[0][0], 6)
    x2[1][0] = round(x2[1][0], 6)
    print('Iter0:')
    print(x2)
    print('Dif0:')
    print(abs(x1[0] - x2[0]))
    print()
    while abs(x1[0] - x2[0]) > eps:
        x1 = x2
        x2 = x1 - J(x1[0], x1[1]).dot(fun(x1[0], x1[1]))
        x1[0][0] = round(x1[0][0], 6)
        x1[1][0] = round(x1[1][0], 6)
        x2[0][0] = round(x2[0][0], 6)
        x2[1][0] = round(x2[1][0], 6)
        print('Iter:')
        print(x2)
        print('Dif:')
        print(abs(x1[0] - round(float(x2[0]), 8)))
        print()


def f1(x, y):
    res = 32 * x * ((0.4*x**2)+y**2-0.5)/5 + (2*y*((math.tan(x*y))**2 + 1)-4*x) * (- x**2 + math.tan(x*y))
    # print(res)
    return res


def f2(x, y):
    res = 2*x*(-x**2 + math.tan(x*y))*((math.tan(x*y)) ** 2 + 1) + 16*y*(0.4*x**2 + y**2-0.5)
    # print(res)
    return res


def iter2(x, y):
    x1 = np.array([[x], [y]])
    x2 = x1 - alfa*np.array([[f1(x1[0][0], x1[1][0])],
                            [f2(x1[0][0], x1[1][0])]])
    print('Iter0:')
    print(x2)
    print()
    ch = 1
    while abs(x1[0] - x2[0]) > eps:
        x1 = x2
        x2 = x1 - alfa * \
            np.array([[f1(x1[0][0], x1[1][0])], [f2(x1[0][0], x1[1][0])]])
        print('Iter:')
        print(x2)
        print()
        ch = ch + 1
    print('res:')
    print(ch)


# fun(xx1, xx2)
# J(xx1. xx2)
#iter(xx1, xx2)
iter2(xx1,xx2)
