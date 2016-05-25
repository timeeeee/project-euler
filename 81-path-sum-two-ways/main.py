"""
Problem 81- Path sum: two ways

Given a matrix, find the minimal sum following a path from the top-left to the
bottom-right corners, only moving to the right or down.

Strategy: Dynamic programming. Go across each row saving the minimal path sum
    to that point.
"""

from sys import argv


def minimal_path_sum(matrix):
    """Find the minimal path sum from top-left to bottom-right in a matrix,
    moving only to the right or down.
    """
    path_sums = [[None for _ in row] for row in matrix]
    height = len(matrix)
    width = len(matrix[0])

    # First row, just add left to right
    path_sums[0][0] = matrix[0][0]
    for column in xrange(1, width):
        path_sums[0][column] = path_sums[0][column - 1] + matrix[0][column]

    for row in xrange(1, height):
        # First column just add from top
        path_sums[row][0] = path_sums[row - 1][0] + matrix[row][0]

        # Then for each, check min(above, left)
        for column in xrange(1, width):
            path_sums[row][column] = min(
                path_sums[row - 1][column],
                path_sums[row][column - 1]) + matrix[row][column]
    return path_sums[-1][-1]


def main():
    if len(argv) == 1:
        print "Usage: python main.py <input_file>"
        exit(1)

    with open(argv[1]) as f:
        matrix = [[int(n) for n in line.split(',')] for line in f]
    print minimal_path_sum(matrix)


if __name__ == "__main__":
    main()
