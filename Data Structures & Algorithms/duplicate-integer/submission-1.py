class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hmap = {}

        for i in range(len(nums)):
            if nums[i] not in hmap:
                hmap[nums[i]] = 1
            else:
                hmap[nums[i]] += 1

        print(hmap)
        
        for key, val in hmap.items():
            if val > 1:
                return True
        return False

