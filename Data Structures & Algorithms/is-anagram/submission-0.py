class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ssorted, tsorted = sorted(s), sorted(t)
        if ssorted != tsorted:
            return False
        return True
        
        