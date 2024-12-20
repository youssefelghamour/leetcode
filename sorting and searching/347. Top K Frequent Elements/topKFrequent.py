class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        
        for n in nums:
            if n not in d:
                d[n] = 0
            d[n] += 1
        
        d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
        lst = list(d.keys())
        
        return lst[:k]