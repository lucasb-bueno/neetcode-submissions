class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        notes:
        - return list of most k frequent numbers in any order

        algorithm:
        - first problem: find how many instances of unique number
            - hashmap to count how many of each unique number we have
        - loop through hashmap and add to arr in tuples (number, times)
        - sort the arr based on the times value
        - set a while the res len(list) is < k, then pop from the arr into res
        - return res

        """

        counter = {}
        for n in nums:
            counter[n] = counter.get(n, 0) + 1

        arr = []
        for number, times in counter.items():
            arr.append((times, number))
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])

        return res


