class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        notes: 
        - always two strings, only lowercase english letters
        - need to have the same lenght
        - return true or false

        brute force: 
        - check if lenght are equal, if not return false
        - sort both, if they're equal, return true
        - complexity: O(n*log(n))

        algorithm:
        

        """

        if (len(s) != len(t)):
            return False
        
        return sorted(t) == sorted(s)

