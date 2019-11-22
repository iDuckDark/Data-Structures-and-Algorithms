"""
Given a matrix of 1s and 0s, count the number of islands. An island is
surrounded by water and is formed by connecting adjacent lands horizontally
or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:
11110
11010
11000
00000
Answer: 1
Example 2:
11000
11000
00100
00011
Answer: 3

Found in:
    https://leetcode.com/problems/number-of-islands/
"""
from typing import List


def count_islands(grid: List[List[str]]) -> int:
    """
    Args:
        grid: a 2d list of 1s or 0s
    Returns:
        the number of islands in the grid

    Time: O(n)
    """

    def dfs(i, j):
        """ do a depth first search in grid at (i,j) """
        if i in range(len(grid)) and j in range(len(grid[0])) and grid[i][j] == "1":
            grid[i][j] = "0"  # mark the cell as visited
            for pos in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                dfs(*pos)
            return 1
        return 0

    return sum(dfs(i, j) for i in range(len(grid)) for j in range(len(grid[0])))


def test():
    """run test cases"""
    tests = ("11000\n11000\n00100\n00011", "11110\n11010\n11000\n00000")
    for testcase in tests:
        grid = [list(line) for line in testcase.splitlines()]
        print(count_islands(grid))


if __name__ == "__main__":
    test()
