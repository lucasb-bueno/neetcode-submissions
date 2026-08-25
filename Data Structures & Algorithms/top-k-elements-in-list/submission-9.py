class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        notes:
        - return a list of the k most frequent elements: [k1, k2]
        - any order

        brute force:
        - building a hashmap where the key is the number and value is the freq
        - run through the hashmap, taking the max value of it until k 

        """
        if k > len(nums):
            return []

        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = count.get(n, 0) + 1
        for number, times in count.items():
            freq[times].append(number)
        
        res = []
        for i in range(len(freq) - 1, 0, - 1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res



        
        
        