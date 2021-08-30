from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        length = len(temperatures)
        res = [0] * length
        for i in range(length):
            while stack and temperatures[i] > stack[-1]:
                top = stack.pop()
                res[top] = i - top
            stack.append(i)
        return res
