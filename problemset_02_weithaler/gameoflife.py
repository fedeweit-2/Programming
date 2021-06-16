# Program for playing the game of Life.
from life import LifeGrid
from life import evolve

# Define the initial configurations of live cells, for the cases of assignment 4.
INIT_CONFIG_0 = [(1, 1), (1, 2), (2, 2), (3, 2)]
INIT_CONFIG_1 = [(1, 3), (2, 2), (3, 1)]
INIT_CONFIG_2 = [(0, 0), (0, 4), (1, 1), (1, 3), (2, 2), (3, 1), (3, 3), (4, 0), (4, 4)]
INIT_CONFIG_3 = [(0, 1), (0, 3), (1, 1), (1, 3), (2, 1), (2, 3), (3, 1), (3, 3), (4, 0), (4, 1), (4, 3), (4, 4)]
INIT_CONFIG_4 = [(r, c) for r in range(0, 5) for c in range(0, 5)]
INIT_CONFIG_5 = [(2, c) for c in range(0, 5)] + [(r, 2) for r in range(0, 5)]
INIT_CONFIG_6 = [(0, 0), (0, 1), (0, 3), (0, 4), (1, 1), (1, 3), (3, 1), (3, 3), (4, 0), (4, 1), (4, 3), (4, 4)]

# Case with a 13x13 grid!
INIT_CONFIG_7 = [(0, 0), (0, 1), (1, 0), (1, 2), (3, 2), (3, 4), (5, 4),
                 (5, 6), (7, 6), (7, 8), (9, 8), (9, 10), (11, 10), (11, 12), (12, 11), (12, 12)]

# We came up with this configuration together as a class, this is why could result similar


# Set the size of the grid.
GRID_WIDTH = 13
GRID_HEIGHT = 13

# Indicate the number of generations.
NUM_GENS = 10


def main():
    # Construct the game grid and configure it.
    grid = LifeGrid(GRID_WIDTH, GRID_HEIGHT)
    grid.configure(INIT_CONFIG_7)

    # Play the game.
    draw(grid)
    for i in range(NUM_GENS):
        evolve(grid, )
        draw(grid)


# Prints a text-based representation of the game grid.
def draw(grid):
    for i in range(grid.numRows()):
        for j in range(grid.numCols()):
            if grid.isLiveCell(i, j):
                print('#', sep=' ', end=' ')
            else:
                print('.', sep=' ', end=' ')
        print('\n')
    print("- next generation -")


# Executes the main routine.
main()
