class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1

        while L <= R:
            middle = (L + R) // 2
            if target > nums[middle]:
                L = middle + 1
            elif target < nums[middle]:
                R = middle - 1
            else:
                return middle
        return -1
