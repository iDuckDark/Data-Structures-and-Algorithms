"""
flood fill
"""
from pprint import pprint


def floodfill(matrix, i, j, before=0, after=1):
    """flood fill algorithm"""
    if matrix[i][j] == before:
        matrix[i][j] = after
        if i > 0:
            floodfill(matrix, i - 1, j, before, after)
        if i < len(matrix[j]) - 1:
            floodfill(matrix, i + 1, j, before, after)
        if j > 0:
            floodfill(matrix, i, j - 1, before, after)
        if j < len(matrix) - 1:
            floodfill(matrix, i, j + 1, before, after)


def test():
    """run test cases"""
    matrix = [
        [0, 0, 0, 0, 2, 2],
        [0, 2, 2, 0, 0, 0],
        [0, 0, 2, 0, 2, 2],
        [2, 0, 2, 0, 0, 2],
        [0, 2, 0, 0, 2, 0],
        [0, 0, 2, 0, 0, 0],
    ]

    floodfill(matrix, 4, 2)
    pprint(matrix)


if __name__ == "__main__":
    test()
