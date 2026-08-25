class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        res = 0
        hset = set()

        for R in range(len(s)):
            while s[R] in hset:
                hset.remove(s[L])
                L += 1
            hset.add(s[R])
            res = max(res, R - L + 1)
        
        return res