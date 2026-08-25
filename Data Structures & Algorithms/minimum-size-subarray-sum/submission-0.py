class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        currSum = 0
        minLength = float('inf')

        for R in range(len(nums)):
            currSum += nums[R]

            while currSum >= target:
                minLength = min(minLength, R - L + 1)
                currSum -= nums[L]
                L += 1
        
        if minLength == float('inf'):
            return 0
        else:
            return minLength