class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        notes:
        example: [3, 6, 7] -> [42, 21, 18]
        only 32bit integer
        brute force:
        init an empty array with n size
        loop through the array n times
        loop again over it and skip i, then take i + 1, i + 2...
        keep multiplying then and adding to a variable
        at the end, add the result to the arr at index i

        O(n2)

        optimal solution:
        
        """

        result = [0] * len(nums)
        for i in range(len(nums)):
            temp = 1
            for j in range(len(nums)):
                if i != j:
                    temp*= nums[j]
            print(temp)
            result[i] = temp
        return result
