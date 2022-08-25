class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        max = 0
        for k in range(1, len(sequence) // len(word) + 1):
            wordK = word * k
            if wordK in sequence:
                max = k
            else:
                return max
        return max

        # max = 0
        # lenWord = len(word)
        # i = 0
        # curr = 0
        # while i < len(sequence):
        #     if i + lenWord < len(sequence):
        #         if sequence[i : i + lenWord] == word:
        #             curr += 1
        #             i += lenWord
        #             if curr > max:
        #                 max = curr
        #         else:
        #             curr = 0
        #             i += 1
        #     else:
        #         return max
        # return max
        # for i in range(len(sequence)):
        #     if sequence[i : i + lenWord] == word:
        #         max += 1
        # return max


testCases = [("ababc", "ab"), ("aaabaaaabaaabaaaabaaaabaaaabaaaaba", "aaaba")]
s = Solution()
for t in testCases:
    print(s.maxRepeating(t[0], t[1]))
