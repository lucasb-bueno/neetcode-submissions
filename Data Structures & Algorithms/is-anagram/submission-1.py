class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        smap = {}
        tmap = {}
        for i in range(len(s)):
            if s[i] not in smap:
                smap[s[i]] = 1
            if t[i] not in tmap:
                tmap[t[i]] = 1

        for j in range(len(s)):
            if s[j] in smap:
                smap[s[j]] += 1
            if t[j] in tmap:
                tmap[t[j]] += 1
        
        print(smap)
        print(tmap)
        
        if smap == tmap:
            return True
            
        return False