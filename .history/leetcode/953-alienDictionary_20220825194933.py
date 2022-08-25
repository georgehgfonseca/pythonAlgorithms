from operator import indexOf
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) < 2:
            return True
        for i in range(len(words) - 1):
            # compare i-th word with i+1-th word
            for j in range(0, min(len(words[i]), len(words[i + 1]))):
                idxI = order.find(words[i][j])
                idxI1 = order.find(words[i + 1][j])
                if idxI > idxI1:
                    return False
                elif idxI < idxI1:
                    break
        return True

        # for i in range(len(order)):
        #     for j in range(i + 1, len(order)):
        #         idxs = []
        #         for k in range(len(words)):
        #             if order[i:j] == words[k][0 : j - i]:
        #                 if len(idxs) == 0:
        #                     idxs.append(k)
        #                 else:
        #                     if idxs[-1] > k:
        #                         return False

        # return True


testCases = [
    (["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"),
    (["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"),
]
s = Solution()
for t in testCases:
    print(s.isAlienSorted(t[0], t[1]))
