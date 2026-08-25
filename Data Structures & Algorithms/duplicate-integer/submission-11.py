class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        notes: 
        - return true if one value appears more than once

        algorithm:
        - for loop thought the arr
        - checking if the value is in hashset
        - yes? return true
        - no? add the value to hashset
        - if ended loop without reuturning true, return false

        """

        hset = set()
        for num in nums:
            if num in hset:
                return True
            hset.add(num)
        return False