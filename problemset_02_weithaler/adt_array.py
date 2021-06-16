# Implements the Array ADT using array capabilities of the ctypes module.
import ctypes


class Array:

    # Creates an array with size elements.
    def __init__(self, size):
        assert size > 0, "Array size must be > 0"
        self._size = size
        # Create the array structure using the ctypes module.
        py_array_type = ctypes.py_object * size
        self._elements = py_array_type()
        # Initialize each element.
        self.clear(None)

    # Returns the size of the array.
    def __len__(self):
        return self._size

    # Gets the contents of the index element.
    def __getitem__(self, index):
        assert 0 <= index < len(self), "Array subscript out of range"
        return self._elements[index]

    # Puts the value in the array element at index position.
    def __setitem__(self, index, value):
        assert 0 <= index < len(self), "Array subscript out of range"
        self._elements[index] = value

    # Clears the array by setting each element to the given value.
    def clear(self, value):
        for i in range(len(self)):
            self._elements[i] = value

    # Returns the array's iterator for traversing the elements.
    def __iter__(self):
        return _ArrayIterator(self._elements)

    def __str__(self):
        text = "["
        for i in range(self._size):
            text += str(self._elements[i])+" "
        return text+"]"


class _ArrayIterator:

    def __init__(self, the_array):
        self._array_ref = the_array
        self._cur_ndx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._cur_ndx < len(self._array_ref):
            entry = self._array_ref[self._cur_ndx]
            self._cur_ndx += 1
            return entry
        else:
            raise StopIteration


class Array2D:

    # Creates a 2-D array of size numRows x numCols.
    def __init__(self, num_rows, num_cols):
        # Create a 1-D array to store an array reference for each row.
        self._theRows = Array(num_rows)

        # Create the 1-D arrays for each row of the 2-D array.
        for i in range(num_rows):
            self._theRows[i] = Array(num_cols)

    # Returns the number of rows in the 2-D array.
    def num_rows(self):
        return len(self._theRows)

    # Returns the number of columns in the 2-D array.
    def num_cols(self):
        return len(self._theRows[0])

    # Clears the array by setting every element to the given value.
    def clear(self, value):
        for row in self._theRows:
            row.clear(value)

    # Gets the contents of the element at position [i, j]
    def __getitem__(self, ndx_tuple):
        assert len(ndx_tuple) == 2, "Invalid number of array subscripts."
        row = ndx_tuple[0]
        col = ndx_tuple[1]
        assert 0 <= row < self.num_rows() and 0 <= col < self.num_cols(), "Array subscript out of range."
        the1d_array = self._theRows[row]
        return the1d_array[col]

    # Sets the contents of the element at position [i,j] to value.
    def __setitem__(self, ndx_tuple, value):
        assert len(ndx_tuple) == 2, "Invalid number of array subscripts."
        row = ndx_tuple[0]
        col = ndx_tuple[1]
        assert 0 <= row < self.num_rows() and 0 <= col < self.num_cols(), "Array subscript out of range."
        the1d_array = self._theRows[row]
        the1d_array[col] = value
