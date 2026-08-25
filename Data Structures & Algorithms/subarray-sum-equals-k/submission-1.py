class Solution:
    """
    notes:
    - return total of subarrays whose sum == k
    - positive and negative numbers
    - cannot be empty
    - can have different order wiht same numbers

    brute force:
    - checking every possible subarray and see if sum == k
    - O(nˆ2)

    optimal:
    - Prefix sum

    """

    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        prefix_count = {0:1}
        prefix_sum = 0
        
        for num in nums:
            prefix_sum += num

            needed = prefix_sum - k
            if needed in prefix_count:
                total += prefix_count[needed]
            
            prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1

        return total





