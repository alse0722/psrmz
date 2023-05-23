def task1(x0, x1, x2, x3, x4, y0, y1, y2, y3, y4):
    p0 = 1 / ((x0-x1) * (x0-x2) * (x0-x3) * (x0-x4))
    p1 = 1 / ((x1-x0) * (x1-x2) * (x1-x3) * (x1-x4))
    p2 = 1 / ((x2-x0) * (x2-x1) * (x2-x3) * (x2-x4))
    p3 = 1 / ((x3-x0) * (x3-x1) * (x3-x2) * (x3-x4))
    p4 = 1 / ((x4-x0) * (x4-x1) * (x4-x2) * (x4-x3))
    print("p0(x) = ", "%.4f" % p0, " * ", "(x - %.3f)" %
          x1, "(x - %.3f)" % x2, "(x - %.3f)" % x3, "(x - %.3f)" % x4, sep="")
    print("p1(x) = ", "%.4f" % p1, " * ", "(x - %.3f)" %
          x0, "(x - %.3f)" % x2, "(x - %.3f)" % x3, "(x - %.3f)" % x4, sep="")
    print("p2(x) = ", "%.4f" % p2, " * ", "(x - %.3f)" %
          x0, "(x - %.3f)" % x1, "(x - %.3f)" % x3, "(x - %.3f)" % x4, sep="")
    print("p3(x) = ", "%.4f" % p3, " * ", "(x - %.3f)" %
          x0, "(x - %.3f)" % x1, "(x - %.3f)" % x2, "(x - %.3f)" % x4, sep="")
    print("p4(x) = ", "%.4f" % p4, " * ", "(x - %.3f)" %
          x0, "(x - %.3f)" % x1, "(x - %.3f)" % x2, "(x - %.3f)" % x3, sep="")

    l0 = p0 * y0
    l1 = p1 * y1
    l2 = p2 * y2
    l3 = p3 * y3
    l4 = p4 * y4
    print("\nL4(x) = ", "%.4f" % l0, " * ", "(x - %.3f)" % x1, "(x - %.3f)" % x2, "(x - %.3f)" % x3, "(x - %.3f)" % x4, " + %.4f" % l1, " * ",
          "(x - %.3f)" % x0, "(x - %.3f)" % x2, "(x - %.3f)" % x3, "(x - %.3f)" % x4, " + %.4f" % l2, " * ", "(x - %.3f)" % x0, "(x - %.3f)" % x1,
          "(x - %.3f)" % x3, "(x - %.3f)" % x4, " + %.4f" % l3, " * ", "(x - %.3f)" % x0, "(x - %.3f)" % x1, "(x - %.3f)" % x2, "(x - %.3f)" % x4,
          " + %.4f" % l4, " * ", "(x - %.3f)" % x0, "(x - %.3f)" % x1, "(x - %.3f)" % x2, "(x - %.3f)" % x3, sep="")

    x = x1 + x2
    res = -0.4309 * (x - 1.546)*(x - 1.834)*(x - 2.647)*(x - 2.910) - 3.4466 * (x - 0.847)*(x - 1.834)*(x - 2.647)*(x - 2.910) + \
        0.1166 * (x - 0.847)*(x - 1.546)*(x - 2.647)*(x - 2.910) + 0.8118 * (x - 0.847)*(x - 1.546)*(x - 1.834)*(x - 2.910) - \
        0.5639 * (x - 0.847)*(x - 1.546)*(x - 1.834)*(x - 2.647)
    print("\nL4(x1+x2 = %.3f) = " % x, "%.4f" % res, sep="", end="\n\n")


def task2(x0, x1, x2, x3, x4, y0, y1, y2, y3, y4):
    table = [[x0, y0], [x1, y1], [x2, y2], [x3, y3], [x4, y4]]
    size = len(table) - 1
    for i in range(0, len(table) - 1):
        for j in range(0, size):
            table[j].append(round(table[j+1][-1] - table[j][-1], 4))
        size -= 1
    for el in table:
        print(el)
    print()

    table = [[x0, y0], [x1, y1], [x2, y2], [x3, y3], [x4, y4]]
    size = len(table) - 1
    offset = 1
    for i in range(0, len(table) - 1):
        for j in range(0, size):
            res = (table[j+1][-1] - table[j][-1]) / \
                (table[j+offset][0] - table[j][0])
            table[j].append(round(res, 4))
        size -= 1
        offset += 1
    for el in table:
        print(el)
    print()


def task3(x0, x1, x2, x3, x4, y0, y1, y2, y3, y4):
    table = [[x0, y0], [x1, y1], [x2, y2], [x3, y3], [x4, y4]]
    size = len(table) - 1
    offset = 1
    for i in range(0, len(table) - 1):
        for j in range(0, size):
            res = (table[j+1][-1] - table[j][-1]) / \
                (table[j+offset][0] - table[j][0])
            table[j].append(round(res, 4))
        size -= 1
        offset += 1

    x = x1 + x2
    polNewton = table[0][1] + table[0][2]*(x-x0) + table[0][3]*(x-x0)*(
        x-x1) + table[0][4]*(x-x0)*(x-x1)*(x-x2) + table[0][5]*(x-x0)*(x-x1)*(x-x2)*(x-x3)
    print("N4(x) = ", "%.3f" % table[0][1], " + ", "%.4f" % table[0][2], "(x-%.3f)" % x0, " + ", "%.4f" % table[0][3], "(x-%.3f)" % x0, "(x-%.3f)" % x1, " + "
          "%.4f" % table[0][4], "(x-%.3f)" % x0, "(x-%.3f)" % x1, "(x-%.3f)" % x2, " + ", "%.4f" % table[0][5], "(x-%.3f)" % x0, "(x-%.3f)" % x1, "(x-%.3f)" % x2,
          "(x-%.3f)" % x3, sep="")
    print("\nN4(x1+x2 = %.3f) = " % x, round(polNewton, 4), sep="")


def task4(x0, x1, x2, x3, x4, y0, y1, y2, y3, y4):
    u= [[x0, y0], [x1, y1], [x2, y2], [x3, y3], [x4, y4]]
    for i in range(0, 4):
        a = (u[i][1]-u[i+1][1]) / (u[i][0]-u[i+1][0])
        b = u[i][1] - a * u[i][0]
        print('a: ', round(a, 3), ' b: ', round(b, 3))

def task5(x0, x1, x2, x3, x4, y0, y1, y2, y3, y4):
    
    m1 = [[x0**2,x0,1,y1],[x1**2,x1,1,y2],[x2**2,x2,1,y2]]
    m2 = [[x2**2,x2,1,y2],[x3**2,x3,1,y3],[x4**2,x4,1,y4]]

    



    
    print('1: ', round(x0**2,3), ' ', x0, ' 1 ', y0)
    print('2: ', round(x1**2,3), ' ', x1, ' 1 ', y1)
    print('3: ', round(x2**2,3), ' ', x2, ' 1 ', y2)



    print('4: ', round(x2**2,3), ' ', x2, ' 1 ', y2)
    print('5: ', round(x3**2,3), ' ', x3, ' 1 ', y3)
    print('6: ', round(x4**2,3), ' ', x4, ' 1 ', y4)

    

def main(x0, x1, x2, x3, x4, y0, y1, y2, y3, y4):
    print('task1')
    task1(x0, x1, x2, x3, x4, y0, y1, y2, y3, y4)
    print('task2')
    task2(x0, x1, x2, x3, x4, y0, y1, y2, y3, y4)
    print('task3')
    task3(x0, x1, x2, x3, x4, y0, y1, y2, y3, y4)
    print('task4')
    task4(x0, x1, x2, x3, x4, y0, y1, y2, y3, y4)
    print('task5')
    task5(x0, x1, x2, x3, x4, y0, y1, y2, y3, y4)


if __name__ == "__main__":
    #main(0.351, 0.867, 3.315, 5.013, 6.432, -0.572, -2.015, -3.342, -5.752, -6.911)
    #main(0.351, 0.867, 1.315, 2.013, 2.859, 0.605, 0.218, 0.205, 1.157, 5.092)
    task5(0.351, 0.867, 1.315, 2.013, 2.859, 0.605, 0.218, 0.205, 1.157, 5.092)
