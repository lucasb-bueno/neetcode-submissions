class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        res = 0
        count = {}

        for R in range(len(s)):
            count[s[R]] = 1 + count.get(s[R], 0)
            res = max(res, count[s[R]])

            if (R - L + 1) - res > k:
                count[s[L]] -= 1 
                L += 1
        return (R - L + 1)
