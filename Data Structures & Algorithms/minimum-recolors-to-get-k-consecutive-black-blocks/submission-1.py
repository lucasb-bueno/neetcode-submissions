class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        """
        notes:
        - return minimum operations with at least one occurence of consecutive black blocks
        - consecutive: window
        - blocks: `W` or `B`
        - at least k operations should be reached

        "WWWBBWBBWWBB" 5 -> "WWWBBBBBWWBB" 1op 
         ------... while R - L + 1 < k

         - if it's W -> add to currCount
         - after reaching k, set res = min(res, currCount)

        """

        res = k
        L = 0
        ops = 0
        for R in range(len(blocks)):
            if blocks[R] == 'W':
                ops += 1
            if R - L + 1 == k:
                res = min(res, ops)
                if blocks[L] == 'W':
                    ops -= 1
                L += 1
        return res
