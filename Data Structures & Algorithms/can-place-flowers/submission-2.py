class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        notes:
        - return True if flowers can be placed in flowerbed
        with no adjecent rule given n flowers needed

        - looping over arr, if ith is == 1, try their neighbors, checking edge issues
        - sum += 1 to temp var and check if <= n
        """
        if n == 0:
            return True
        
        possibleFlowers = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                prev = (i == 0 or flowerbed[i - 1] == 0)
                nxt = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
                
                if prev and nxt:
                    flowerbed[i] = 1
                    possibleFlowers += 1
        return possibleFlowers >= n