class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hs = set()

        for i in nums:
            hs.add(i)
        
        return len(hs) != len(nums)
        