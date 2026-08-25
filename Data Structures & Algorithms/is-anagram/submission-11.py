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

        optimal O(n):
        - check if lenght are equal, if not return false
        - create two hashmaps, (map(s), map(t))
        - two for loops, check if the key is in the map
        - compare if maps are equal

        """

        smap = {}
        tmap = {}

        if len(s) != len(t):
            return False

        for c in s:
            smap[c] = smap.get(c, 0) + 1
        
        for c in t:
            tmap[c] = tmap.get(c, 0) + 1

        
        return smap == tmap

         

