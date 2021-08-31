class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pre_sum = {0: 1}
        ans, cur_sum = 0, 0
        for n in nums:
            cur_sum += n
            mod_n = cur_sum % k
            ans += pre_sum.get(mod_n, 0)
            pre_sum[mod_n] = pre_sum.get(mod_n, 0) + 1
        return ans
