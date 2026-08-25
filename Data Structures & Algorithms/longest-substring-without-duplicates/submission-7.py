class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        notes:
        - return lenght -> longest substring without repeating
        - s -> ASCII 
        - sliding window
        - set var longest = 0
        - L and R starting at zero
        - loop from 0 to len(s) + 1
        - while 

        """

        charSet = set()
        L = 0
        length = 0

        for R in range(len(s)):
            while s[R] in charSet:
                charSet.remove(s[L])
                L += 1
            charSet.add(s[R])
            length = max(length, R - L + 1)
        return length




