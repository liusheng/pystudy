class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_sum = []
        hash_sum = {}
        abs_k = abs(k)
        for i, n in enumerate(nums):
            if not prefix_sum:
                sum_n = n
            else:
                sum_n = prefix_sum[i - 1] + n
            if sum_n not in hash_sum:
                hash_sum[sum_n] = i
            prefix_sum.append(sum_n)
        for i in range(1, len(prefix_sum)):
            n = 0
            tmp_sum = prefix_sum[i] - n * abs_k
            while tmp_sum >= 0:
                if tmp_sum in hash_sum and (i - hash_sum[tmp_sum] >= 2):
                    return True
                elif (abs_k != 0 and tmp_sum % abs_k == 0) and i >= 1:
                    return True
                elif abs_k == 0 and tmp_sum == 0 and i >= 1:
                    return True
                if abs_k == 0:
                    break
                n += 1
                tmp_sum = prefix_sum[i] - n * abs_k
        return False