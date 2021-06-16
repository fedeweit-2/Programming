# from matrix import matrix_adt

class SparseMatrix:
    # Create a sparse matrix of size numRows x numCols initialized to 0.
    def __init__(self, numRows, numCols):
        self._numRows = numRows
        self._numCols = numCols
        self._elementList = list()

    # Return the no of rows in matrix
    def numRows(self):
        return self._numRows

    # Return the number of columns in the matrix
    def numCols(self):
        return self._numCols

    # Return the value of element (i,j):x[i,j]
    def __getitem__(self, ndxTuple):
        ndx = self._findPosition(ndxTuple[0], ndxTuple[1])
        if ndx is None:
            return 0
        return self._elementList[ndx].value

    # Set the value of element i,j to the value s: x[i,j] = s
    def __setitem__(self, ndxTuple, scalar):
        ndx = self._findPosition(ndxTuple[0], ndxTuple[1])
        if ndx is not None:
            if scalar != 0.0:
                self._elementList[ndx].value = scalar
            else:
                self._elementList.pop(ndx)
        else:
            if scalar != 0.0:
                element = _MatrixElement(ndxTuple[0], ndxTuple[1], scalar)
                self._elementList.append(element)

    # Scale by the given scalar
    def scaleBy(self, scalar):
        for item in self._elementList:
            item.value *= scalar

    # Additional methods
    def __add__(self, rhsMatrix):
        assert rhsMatrix.numRows() == self.numRows() and \
               rhsMatrix.numCols() == self.numCols(), "Matrix not compatible"

        newMatrix = SparseMatrix(self.numRows(), self.numCols())

        for element in self._elementList:
            dupElement = _MatrixElement(element.row, element.col, element.value)
            newMatrix._elementList.append(dupElement)

        for element in rhsMatrix._elementList:
            print(element.row, element.col)
            value = newMatrix[element.row, element.col]
            value += element.value
            newMatrix[element.row, element.col] = value

        return newMatrix

    def __sub__(self, rhsMatrix):
        assert rhsMatrix.numRows() == self.numRows() and \
               rhsMatrix.numCols() == self.numCols(), "Matrix not compatible"

        newMatrix = SparseMatrix(self.numRows(), self.numCols())

        for element in self._elementList:
            dupElement = _MatrixElement(element.row, element.col, element.value)
            newMatrix._elementList.append(dupElement)

        for element in rhsMatrix._elementList:
            value = newMatrix[element.row, element.col]
            value -= element.value
            newMatrix[element.row, element.col] = value

        return newMatrix

    def __mul__(self, rhsMatrix):
        assert rhsMatrix.numRows() == self.numCols(), "Matrix not compatible"

        newMatrix = SparseMatrix(rhsMatrix.numRows(), self.numCols())

        for element in self._elementList:
            tmpElement = _MatrixElement(element.row, element.col, element.value)
            newMatrix._elementList.append(tmpElement)

        for element in rhsMatrix._elementList:
            value = newMatrix[element.row, element.col]
            value *= element.value
            newMatrix[element.row, element.col] = value

        return newMatrix

    def transpose(self):
        pass

    # Added str magic method to print the output
    def __str__(self):
        text = ""
        for r in range(self.numRows()):
            text += "\n"
            for c in range(self.numCols()):
                text += f"{m_sum[r, c]} "
        return text

    def _findPosition(self, row, col):
        n = len(self._elementList)
        for i in range(n):
            if row == self._elementList[i].row and \
                    col == self._elementList[i].col:
                return i  # return the index of the element if found.
        return None  # return None when the element is zero.


# Storage class for holding non-zero matrix elements
class _MatrixElement:
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value


if __name__ == '__main__':
    m1 = SparseMatrix(5, 5)
    m2 = SparseMatrix(5, 5)

    m1[0, 0] = 2
    m2[0, 0] = 3

    m_sum = m1 * m2

    print(m_sum)
