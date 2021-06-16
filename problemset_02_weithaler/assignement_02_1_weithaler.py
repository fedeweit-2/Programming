from adt_matrix import Matrix

if __name__ == '__main__':

    # Creating array 1
    m = Matrix(3, 2)
    k = 0
    for i in range(m.numRows()):
        for j in range(m.numCols()):
            m.__setitem__([i, j], k)
            k += 1

    # Creating array 2
    m1 = Matrix(3, 2)
    k = 6
    for i in range(m1.numRows()):
        for j in range(m1.numCols()):
            m1.__setitem__([i, j], k)

    print("Transpose")
    m2 = m.tranpose()
    print(m2)

    print("Subtract m1 to m")
    m3 = m1.__sub__(m)

    print("m:")
    print(m)

    print("m1:")
    print(m1)

    print("Sub:")
    print(m3)

    # Creating array 3
    mA = Matrix(3, 2)
    k = 0
    for i in range(mA.numRows()):
        for j in range(mA.numCols()):
            mA.__setitem__([i, j], k)
            k += 1

    # Creating array 4
    mB = Matrix(2, 3)
    k = 6
    for i in range(mB.numRows()):
        for j in range(mB.numCols()):
            mB.__setitem__([i, j], k)

    print("Multiply mA for mB")

    print("mA:")
    print(mA)

    print("mB:")
    print(mB)

    m4 = mA.__mul__(mB)
    print("Mul:")
    print(m4)
