class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        if n - 1 in list, if its not, it is the beggining of a sequence
        while n + 1 in the list: increment a variable 
        insert nums into a set() data structure

        """
        maxSeq = 0
        hset = set(nums)

        for num in nums:
            if num - 1 not in hset:
                length = 1
                while num + length in hset:
                    length += 1
                maxSeq = max(length, maxSeq)
        return maxSeq    

