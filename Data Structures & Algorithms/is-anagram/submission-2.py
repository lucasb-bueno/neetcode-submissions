class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        smap, tmap = {}, {}

        for i in range(len(s)):
            if s[i] not in smap:
                smap[s[i]] = 1
            if t[i] not in tmap:
                tmap[t[i]] = 1
        for i in range(len(s)):
            if s[i] in smap:
                smap[s[i]] += 1
            if t[i] in tmap:
                tmap[t[i]] += 1
        
        return smap == tmap
