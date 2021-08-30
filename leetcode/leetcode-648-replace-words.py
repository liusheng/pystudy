from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = {}
        sorted_dict = sorted(dictionary)
        for d in sorted_dict:
            tmp_d = trie
            dup = True
            for c in d:
                if c in tmp_d and tmp_d[c] == {} and dup:
                    break
                elif c not in tmp_d:
                    dup = False
                    tmp_d[c] = {}
                tmp_d = tmp_d[c]

        ret = []
        for word in sentence.split(" "):
            tmp_d2 = trie
            root_cur = []
            for c in word:
                if c in tmp_d2:
                    root_cur.append(c)
                    if tmp_d2[c] == {}:
                        ret.append(''.join(root_cur))
                        break
                    tmp_d2 = tmp_d2[c]
                else:
                    ret.append(word)
                    break
            else:
                ret.append(word)
        return " ".join(ret)