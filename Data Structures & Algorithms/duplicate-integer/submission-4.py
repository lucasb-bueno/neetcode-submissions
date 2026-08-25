class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hmap = {}

        for i in range(len(nums)):
            if nums[i] not in hmap:
                hmap[nums[i]] = 1
            else:
                hmap[nums[i]] += 1
        
        for key, value in hmap.items():
            if value > 1:
                return True
        return False

        