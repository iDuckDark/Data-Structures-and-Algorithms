"""
A very hungry rabbit is placed in the center of of a garden,
represented by a rectangular N x M 2D matrix. The values of the
matrix will represent numbers of carrots available to the rabbit
in each square of the garden. If the garden does not have an
exact center, the rabbit should start in the square closest to
the center with the highest carrot count.

On a given turn, the rabbit will eat the carrots available on the
square that it is on, and then move up, down, left, or right,
choosing the the square that has the most carrots. If there are no
carrots left on any of the adjacent squares, the rabbit will go to
sleep. You may assume that the rabbit will never have to choose
between two squares with the same number of carrots.

Write a function which takes a garden matrix and returns the number
of carrots the rabbit eats. You may assume the matrix is rectangular
with at least 1 row and 1 column, and that it is populated with
non-negative integers. For example,

[[5, 7, 8, 6, 3],
 [0, 0, 7, 0, 4],
 [4, 6, 3, 4, 9],
 [3, 1, 0, 5, 8]]
-> 27
"""


def get_max_point(board, points):
    """return the point with the largest value on the board"""
    best_point = (-1, -1)
    best = 0
    for i, j in points:
        if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] > best:
            best_point = (i, j)
            best = board[i][j]
    return best_point


def solve(board):
    """Solve the carrot problem"""
    # Get the possible starting points on the board
    starting_points = [
        ((len(board) - i) // 2, (len(board[0]) - j) // 2)
        for i in (0, 1)
        for j in (0, 1)
    ]
    total = 0
    i, j = get_max_point(board, starting_points)
    while (i, j) != (-1, -1):
        total += board[i][j]
        board[i][j] = 0  # collect the carrots
        neighbours = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
        i, j = get_max_point(board, neighbours)
    return total


def test():
    """test cases"""
    board = [[5, 7, 8, 6], [0, 0, 7, 0], [4, 6, 3, 4], [3, 1, 0, 5], [5, 7, 8, 6]]
    assert solve(board) == 78

    board = [
        [5, 7, 8, 6, 3],
        [0, 0, 7, 0, 4],
        [4, 6, 3, 4, 9],
        [3, 1, 0, 5, 8],
        [5, 7, 8, 6, 3],
    ]
    assert solve(board) == 30

    board = [[5, 7, 8, 6, 3], [0, 0, 7, 0, 4], [4, 6, 3, 4, 9], [3, 1, 0, 5, 8]]
    assert solve(board) == 27

    board = [[5, 7, 8, 6], [10, 0, 7, 0], [4, 6, 3, 4], [3, 1, 0, 5]]
    assert solve(board) == 59


if __name__ == "__main__":
    test()
