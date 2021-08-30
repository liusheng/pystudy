class Solution:
    def __init__(self):
        self.res = 0

    def totalNQueens(self, n: int) -> int:
        self.n_queens([], n)
        return self.res

    def n_queens(self, res_one, n):
        cur_len = len(res_one)
        if cur_len == n:
            self.res += 1
            return
        for i in range(n):
            if i not in res_one:
                for row, col in enumerate(res_one):
                    if abs(cur_len - row) == abs(i - col):
                        break
                else:
                    res_one.append(i)
                    self.n_queens(res_one, n)
                    res_one.pop()
