class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curComb, curSum):
            # Base case 1
            if curSum == target:
                res.append(curComb.copy())
                return
            
            # Base case 2
            if curSum > target or i >= len(nums):
                return
            
            # Choice 1
            curComb.append(nums[i])
            dfs(i, curComb, curSum + nums[i])
            curComb.pop()

            # Choice 2
            dfs(i + 1, curComb, curSum)
        
        dfs(0, [], 0)

        return res