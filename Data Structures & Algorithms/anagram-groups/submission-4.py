class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        - return a list of lists with anagrams of each other
        - Hashmap counter
        - lowercase letters -> [] len(26)
        - ord() to get the number of that char and used it as an index 
        in our hashmap
        

        Pseudocode:
        - hashmap with a list as the key
        - res = []
        - for loop in each list item
        - instance the 26 size list
        - for loop to get each character in the word
        - get the index = ord(char) - ord("a")
        - add 1 to hashmap value into that index
        - add to the res list the item in the hashmap 
        - after the char loop, we add the list as a value of the hashmap

        """

        hmap = defaultdict(list)

        for word in strs:
            wordmap = [0] * 26
            for char in word:
                index = ord(char) - ord('a')
                wordmap[index] += 1
            hmap[tuple(wordmap)].append(word)

        return hmap.values()
        



