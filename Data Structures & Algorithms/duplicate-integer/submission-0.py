class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr = []
        for i in nums:
            if i not in arr:
                arr.append(i)
            else:
                return True
        return False