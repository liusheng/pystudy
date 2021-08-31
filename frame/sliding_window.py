import collections


def sliding_window(s: str, t: str):
    ans = []

    need = dict(collections.Counter(t))
    left, right = 0, 0
    need_len = len(need)
    t_len = len(t)
    valid = 0
    window = {}

    while right < len(s):
        window[s[right]] = window.get(s[right], 0) + 1
        if window[s[right]] == need.get(s[right]):
            valid += 1
        right += 1
        if right - left == t_len:
            if valid == need_len:
                ans.append(left)
            if window[s[left]] == need.get(s[left]):
                valid -= 1
            window[s[left]] -= 1
            left += 1
    return ans
