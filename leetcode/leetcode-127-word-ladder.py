import collections


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        word_dict = {}
        len_word = len(beginWord)
        for word in wordList:
            for i in range(len_word):
                sub_word = word[:i]+word[(i+1):]+str(i)
                if sub_word not in word_dict:
                    word_dict[sub_word] = [word]
                else:
                    word_dict[sub_word].append(word)

        queen = collections.deque()
        queen.append(beginWord)
        visited = {beginWord}
        ret = 1
        while queen:
            length = len(queen)
            for _ in range(length):
                cur = queen.popleft()
                if cur == endWord:
                    return ret
                for i in range(len(cur)):
                    sub_cur = cur[:i]+cur[(i+1):]+str(i)
                    if sub_cur not in word_dict:
                        continue
                    for word in word_dict[sub_cur]:
                        if word not in visited:
                            queen.append(word)
                            visited.add(word)
            ret += 1
        return 0
