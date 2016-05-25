# How many routes are there from one corner of a 20x20 grid to the opposite corner,
# only traveling right or down along grid lines?

def pathsNxN(n):
    grid = [[0 for _ in range(n)] for _ in range(n)]
    return pathsTo(grid, n - 1, n - 1)

# Paths to a point are sum of paths to both successive points
# Save solutions to points as we go and check for previous answers before calculating new ones
def pathsTo(grid, x, y):
    if x < 0 or y < 0: return 1
    elif grid[x][y]:
        return grid[x][y]
    else:
        paths = pathsTo(grid, x - 1, y) + pathsTo(grid, x, y - 1)
        grid[x][y] = paths
        return paths

if __name__ == "__main__":
    print pathsNxN(20)
