class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cset = set()
        L = 0
        res = 0

        for R in range(len(s)):
            while s[R] in cset:
                cset.remove(s[L])
                L += 1
            cset.add(s[R])
            res = max(res, R - L + 1)
        return res