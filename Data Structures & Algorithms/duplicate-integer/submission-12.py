class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        items = set(nums)

        if len(items) != len(nums):
            return True
        
        return False
        
        