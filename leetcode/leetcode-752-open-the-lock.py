from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == '0000':
            return 0
        if '0000' in deadends:
            return -1
        visited = {'0000'}
        dead = set(deadends)
        first_set, second_set = {'0000'}, {target}
        res = 0
        while first_set:
            res += 1
            if len(first_set) > len(second_set):
                first_set, second_set = second_set, first_set
            tmp_set = set()
            for num in first_set:
                for i in range(4):
                    for d in (-1, 1):
                        new_n = num[:i] + str((int(num[i])+d) % 10) + num[i+1:]
                        if new_n in second_set:
                            return res
                        if new_n not in dead and new_n not in visited:
                            tmp_set.add(new_n)
                            visited.add(new_n)
            first_set = tmp_set
        return -1
