class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        
        for num in nums:
            if num in d:
                del d[num]
            else:
                d[num] = 1
        
        return list(d.keys())[0]