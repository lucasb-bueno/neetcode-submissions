class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hset = set(nums)
        return len(hset) != len(nums)

         