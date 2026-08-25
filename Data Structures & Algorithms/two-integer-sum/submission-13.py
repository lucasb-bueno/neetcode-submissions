class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        notes:
        - return a list of two indicies where the sum of them is equal to target
        - exactly one pair (just return when we find the result)
        - we cannot use the same items in same index to sum

        algorithm:
        - hashmaps to store the num as keys and index as values
        - calculate the diff between the number we are and the target
        - check if diff is in hashmap
        - yes? take the value of this diff value and the curr one
        - return it in a list
        - no? add the diff into the hashmap and the index

        """

        hmap = {}
        for i, num in enumerate(nums):
            diff = target - num
            if (diff in hmap):
                return [hmap[diff], i]
            hmap[num] = i
        return []

        
