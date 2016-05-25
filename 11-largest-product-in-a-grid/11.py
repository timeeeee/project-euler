"""
What is the greatest product of four adjacent numbers in the same direction
(up, down, left, right, or diagonally) in the 20x20 grid?
"""


def get_grid(filename):
    """Load a space-separated grid from file"""
    with open(filename) as f:
        return [[int(n) for n in line.split()] for line in f]


def prod(seq):
    """Return the product of a sequence"""
    return reduce(lambda x, y: x * y, seq)


def max_product(grid, n):
    """Find the maximum product of n numbers in a grid"""
    max_p = None
    width = len(grid[0])
    height = len(grid)

    # horizontal sequences
    for line in grid:
        for start_col in range(width - n + 1):
            product = prod(line[start_col:start_col + n])
            max_p = max(max_p, product)

    # vertical sequences
    for column in range(width):
        for start_row in range(height - n + 1):
            product = prod(
                grid[start_row + offset][column] for offset in range(4))
            max_p = max(max_p, product)

    # top left to bottom right diagonal sequences
    for start_col in range(width - n + 1):
        for start_row in range(height - n + 1):
            product = prod(grid[start_row + offset][start_col + offset]
                           for offset in range(4))
            max_p = max(max_p, product)

    # top right to bottom left diagonal sequences
    for start_col in range(3, width):
        for start_row in range(height - n + 1):
            product = prod(grid[start_row + offset][start_col - offset]
                           for offset in range(4))
            max_p = max(max_p, product)

    return max_p

if __name__ == "__main__":
    print max_product(get_grid("data.txt"), 4)
