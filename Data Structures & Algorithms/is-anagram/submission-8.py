class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(t) != len(s)):
            return False

        words = [0] * 26
        for i in range(len(s)):
            index = ord(s[i]) - ord('a')
            print(index)
            words[index] += 1
        
        wordt = [0] * 26
        for j in range(len(t)):
            index = ord(t[j]) - ord('a')
            print(index)
            wordt[index] += 1

        print(words)
        print(wordt)

        return words == wordt
        
