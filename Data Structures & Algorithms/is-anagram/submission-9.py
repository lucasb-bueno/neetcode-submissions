class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        notes:
        - return True if s is anagram of t
        - all lowercase english letters (26 possibilities)
        - both need to have the same lenght

        algorithm:
        - build two hashmaps (t and s) 
        - the key is the char and value is the freq of the char
        - - space complxity O(n)

        - build an arr of 26 lenght []
        - each position of the arr is the ord number of an english character
        - check if both arr are equal
        - val index = ord(s[i]) - ord('a')
        - do a loop and place the freq at arr[index]
        - space complxity O(26)
        """

        sFreq = [0] * 26 
        tFreq = [0] * 26

        if len(s) != len(t):
            return False

        for c in range(len(s)):
            index = ord(s[c]) - ord("a")
            sFreq[index] += 1

        for c in range(len(t)):
            index = ord(t[c]) - ord("a")
            tFreq[index] += 1

        print(sFreq)
        print(tFreq)

        return sFreq == tFreq