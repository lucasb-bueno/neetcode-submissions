class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        notes: 
        - two items in list sum up to the target
        - no duplicates
        - nums.lenght up to 10 milion O(n) for the optmial (hint)

        algorithm (optimal):
        - strategy: store the item in HM key and the difference in value
        structure: hash maps {key: diff, value: index}

        hashMap = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashMap:
                return[hashMap[diff], i]
            hashMap[i] = diff
        return []

        """


        hashMap = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[num] = i




