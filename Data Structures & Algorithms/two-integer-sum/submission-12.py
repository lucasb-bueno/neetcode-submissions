class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        notes:
        - return a list of two indicies where the sum of them is equal to target
        - exactly one pair (just return when we find the result)
        - we cannot use the same items in same index to sum

        algorithm:
        - 
        - for loop over nums 

        """

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if (i != j and nums[i] + nums[j] == target):
                    return [i, j]
        return []
