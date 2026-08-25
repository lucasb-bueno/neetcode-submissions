class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        snum = sorted(nums)
        for i in range(1, len(snum)):
            if snum[i] == snum[i - 1]:
                return True
        return False