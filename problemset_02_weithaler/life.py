# Implements the LifeGrid ADT for use with the game of Life.
from adt_array import Array2D

# Generates the next generation of organisms.
def evolve(grid, generation=1):
    for x in range(generation):
        # List for storing the live cells of the next generation.
        liveCells = list()

        # Iterate over the elements of the grid.
        for i in range(grid.numRows()):
            for j in range(grid.numCols()):

                # Determine the number of live neighbors for this cell.
                neighbors = grid.numLiveNeighbors(i, j)

                # Add the (i,j) tuple to liveCells if this cell contains
                # a live organism in the next generation.
                if (neighbors == 2 and grid.isLiveCell(i, j)) or \
                        (neighbors == 3 and grid.isLiveCell(i, j)) or \
                        (not grid.isLiveCell(i, j) and neighbors == 3):
                    liveCells.append((i, j))

        # Reconfigure the grid using the liveCells coord list.
        grid.configure(liveCells)


class LifeGrid:
    # Defines constants to represent the cell states
    DEAD_CELL = 0
    LIVE_CELL = 1

    # Creates the game grid and initializes the cells to dead.
    def __init__(self, numRows, numCols):
        self._grid = Array2D(numRows, numCols)
        self.configure(list())

    def numRows(self):
        return self._grid.num_rows()

    def numCols(self):
        return self._grid.num_cols()

    def configure(self, coordList):
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                self.clearCell(i, j)

        for coord in coordList:
            self.setCell(coord[0], coord[1])

    def isLiveCell(self, row, col):
        return self._grid[row, col] == self.LIVE_CELL

    def clearCell(self, row, col):
        self._grid[row, col] = self.DEAD_CELL

    def setCell(self, row, col):
        self._grid[row, col] = self.LIVE_CELL

    def numLiveNeighbors(self, row, col):
        count = 0
        upper_bound = row - 1 if row > 0 else row
        left_bound = col - 1 if col > 0 else col
        right_bound = col + 1 if col < (self.numCols() - 1) else self.numCols() - 1
        lower_bound = row + 1 if row < (self.numRows() - 1) else self.numRows() - 1

        for i in range(upper_bound, lower_bound + 1):
            for j in range(left_bound, right_bound + 1):
                if i == row and j == col:
                    continue
                if self.isLiveCell(i, j):
                    count += 1
        return count
