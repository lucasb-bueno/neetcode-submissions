class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        notes:
        - return true if palindrome (same backward/forward)
        - case insensitive (does not care)
        - ignores NON alpha numeric
        - Allowed: (A-Z, a-z) and numbers (0-9)

        algorithm:
        - convert and filter: make lowercase, block non alpha numeric
        - use two pointers: start and end, left, right and keep moving them
        - if in certain point they diverge, return False
        - if they L == R: return True

        """

        new = ""
        for i in s.lower():
            if i.isalnum():
                new += i
                
        L = 0
        R = len(new) - 1

        while L < R:
            if new[L] != new[R]:
                return False
            L += 1
            R -= 1

        return True



