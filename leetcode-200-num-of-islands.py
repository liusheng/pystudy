from typing import List


class UF(object):
    def __init__(self, m, n):
        self.count = m * n
        self.parents = [[(i, j) for j in range(n)] for i in range(m)]
        self.size = [[1 for j in range(n)] for i in range(m)]

    def union(self, row1, col1, row2, col2):
        p1 = self.find(row1, col1)
        p2 = self.find(row2, col2)
        if p1 == p2:
            return
        if self.size[row1][col1] >= self.size[row2][col2]:
            self.parents[row2][col2] = p1
            self.size[row1][col1] += self.size[row2][col2]
        else:
            self.parents[row1][col1] = p2
            self.size[row2][col2] += self.size[row1][col1]
        self.count -= 1

    def find(self, row, col):
        while self.parents[row][col] != (row, col):
            self.parents[row][col] = self.parents[self.parents[row][col][0]][
                self.parents[row][col][1]]
            row, col = self.parents[row][col]
        return self.parents[row][col]


class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        uf = UF(m, n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    uf.count -= 1
                    continue
                if grid[i][j] == "1":
                    for h, v in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                        if i + h >= m or i + h < 0 or j + v >= n or j + v < 0:
                            continue
                        if grid[i + h][j + v] == "1":
                            uf.union(i, j, i + h, j + v)
        return uf.count


print(Solution().numIslands(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]))
