class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        notes: 
        - group anagrams in sublist
        - empty strings allowed
        - never zero items
        - not long contraints
        - lowercase english letters

        algorithm:
        - create the res list
        - for each of the words, we pass them throught map parser
        - create the result hashmap (key -> anagram hasmap), value -> list of words)
        - we could store in hashmaps OR with an array of 26 caracters as the key
        - at the end, append the values in the main hashmap into the res list

        """

        res = []
        d = defaultdict(list)

        for word in strs:
            wordmap = [0] * 26
            for letter in word:
                index = ord(letter) - ord('a')
                wordmap[index] += 1
            d[tuple(wordmap)].append(word)

        for key, val in d.items():
            res.append(val)
        
        return res

