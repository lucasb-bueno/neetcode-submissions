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

        if len(s) != len(t):
            return False

        sarr = [0] * 26
        tarr = [0] * 26

        for c in s:
            index = ord(c) - ord("a")
            sarr[index] += 1

        for c in t:
            index = ord(c) - ord("a")
            tarr[index] += 1

        return sarr == tarr
        


        

        
        return smap == tmap

         

