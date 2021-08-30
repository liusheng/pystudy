from typing import List


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        length = len(M)

        class UF(object):
            def __init__(self):
                self.parents = [i for i in range(length)]
                self.size = [1] * length
                self.sum = length

            def find(self, c):
                while self.parents[c] != c:
                    self.parents[c] = self.parents[self.parents[c]]
                    c = self.parents[c]
                return c

            def union(self, first, second):
                first_p = self.find(first)
                second_p = self.find(second)
                if first_p == second_p:
                    return
                if self.size[first_p] > self.size[second_p]:
                    self.parents[second_p] = first_p
                    self.size[first_p] += self.size[second_p]
                else:
                    self.parents[first_p] = second_p
                    self.size[second_p] += self.size[first_p]
                self.sum -= 1

        uf = UF()
        for i in range(length):
            for j in range(i + 1, length):
                if M[i][j] == 1:
                    uf.union(i, j)
        return uf.sum
