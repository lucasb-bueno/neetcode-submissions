class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted = ""

        for char in s.lower():
            if char.isalnum():
                formatted += char
        
        L, R = 0, len(formatted) - 1
        while L <= R:
            if formatted[L] != formatted[R]:
                return False
            L += 1
            R -= 1
        return True
