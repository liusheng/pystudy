import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tar_win = dict(collections.Counter(t))
        tar_len = len(tar_win)
        cur_win = {k: 0 for k in tar_win}
        cur_len = 0
        left, right = 0, 0
        ret = ''

        while right < len(s):
            if s[right] in cur_win:
                cur_win[s[right]] += 1
                if cur_win[s[right]] == tar_win[s[right]]:
                    cur_len += 1
            right += 1
            while cur_len == tar_len:
                if not ret or len(s[left:right]) < len(ret):
                    ret = s[left:right]
                if s[left] in cur_win:
                    if cur_win[s[left]] == tar_win[s[left]]:
                        cur_len -= 1
                    cur_win[s[left]] -= 1
                left += 1
        return ret