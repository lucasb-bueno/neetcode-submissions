class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        
        word = ""

        for i in s.lower():
            if i.isalnum():
                word += i
        
        L, R = 0, len(word) - 1

        for i in range(len(word)):
            while L <= R:
                if word[L] != word[R]:
                    return False
                L += 1
                R -= 1
        return True


        