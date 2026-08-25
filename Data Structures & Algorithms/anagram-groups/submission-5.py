from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        notes:
        - return list of lists where sublists are groups of anagrams
        - any order
        - 26 english lowercase letters

        brute-force:
        - looping over the main list of words
        - solving anagram of each of them creating or hasmap or list of size 26
        - other loop to check which of the lists are equal and group them
        - O(n2) time and O(n2) space

        algorithm:
        - solving the first problem which is solving anagrams
        - create a hashmap where the key is the list of size 26, and values list of words
        - group the hashmap into a list of lists
        """

        hmap = defaultdict(list)
        for word in strs:
            arr = [0] * 26
            for c in word:
                index = ord(c) - ord("a")
                arr[index] += 1
            hmap[tuple(arr)].append(word)
        return list(hmap.values())


