class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hset = set()
        L = 0
        length = 0

        for R in range(len(s)):
            while s[R] in hset:
                hset.remove(s[L])
                L += 1
            hset.add(s[R])
            length = max(length, R - L + 1)
        return length
