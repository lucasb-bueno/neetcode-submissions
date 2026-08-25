class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hset = set()

        for n in nums:
            if n not in hset:
                hset.add(n)
            else:
                return n