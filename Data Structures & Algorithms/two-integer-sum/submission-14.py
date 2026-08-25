class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        notes: 
        - two items in list sum up to the target
        - no duplicates
        - nums.lenght up to 10 milion O(n) for the optmial (hint)

        algorithm (brute force):
        
        for i in range (len(nums) - 1)
            for j in range (len(nums))
                if (nums(i) + nums(j) == target and i != j ):
                    return [i, j]
        return []

        """

        for i in range (len(nums)):
            for j in range (len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i, j]
        return []




