class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        notes:
        - return True if there's an interval abs at size k that contains duplicates
        - sliding window
        - L and R pointers
        - set() to check in O(1) if item is present
        if R - L + 1 > k:
            set.remove(nums[L])
            L += 1
        if nums[L] in set:
            return True
        set.add(nums[L])
        
    return False

        """
        numSet = set()
        L = 0
        for R in range(len(nums)):
            if R - L > k:
                numSet.remove(nums[L])
                L += 1
            if nums[R] in numSet:
                return True
            numSet.add(nums[R])
            
        return False