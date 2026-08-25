class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        notes:
        - retrun array where each item is 
        product of all of the items except himself
        - try to solve in O(n) without using / operator
        - [1,2,4,6] -> [48, 24, 12, 8]
        - does it need to be sorted?

        brute force:
        - run throught the items in O(nˆ2)
        - skip the [i] item
        - add the result in the result arr


        algorithm:
        - build prefix arr of product not excluding anyone
        - take the item and divide all of the items by it
 
        """

        n = len(nums)

        prefix = [0] * n
        sufix = [0] * n
        res = [0] * n

        prefix[0] = sufix[-1] = 1

        for i in range(n - 2, -1, -1):
            sufix[i] = sufix[i + 1] * nums[i + 1]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(n):
            res[i] = sufix[i] * prefix[i]

        return res









