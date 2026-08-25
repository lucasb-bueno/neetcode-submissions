class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        notes:
        - return True if s is anagram of t, false otherwise
        - only lowercase

        algorithm:
        - 

        """
        
        maps = {}
        mapt = {}

        for i in range(len(s)):
            maps[s[i]] = 1 + maps.get(s[i], 0)

        for i in range(len(t)):
            mapt[t[i]] = 1 + mapt.get(t[i], 0)

        return maps == mapt
