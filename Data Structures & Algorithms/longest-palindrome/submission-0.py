class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = {}
        length = 0

        for i in s:
            counter[i] = counter.get(i, 0) + 1
            if counter[i] % 2 == 0:
                length += 2

        for val in counter.values():
            if val % 2 != 0:
                length += 1
                break
        
        return length