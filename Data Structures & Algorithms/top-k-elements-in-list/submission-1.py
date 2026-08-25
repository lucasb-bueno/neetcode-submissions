class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}

        for i in nums:
            if i not in hmap:
                hmap[i] = 1
            else:
                hmap[i] += 1

        sorted_by_values = dict(sorted(hmap.items(), key=lambda item: item[1], reverse = True))
        return list(sorted_by_values.keys())[:k]
        
        
        
            

        
        

