class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        l, r = 0, len(nums)
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                currSum = nums[i] + nums[l] + nums[r]
                if currSum == 0:
                    if [nums[i], nums[l], nums[r]] not in res:
                        res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif currSum < 0:
                    l += 1
                else:
                    r -= 1
        return res
        