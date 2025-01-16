class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        half = len(nums) // 2
        
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        for k,v in counts.items():
            if v > half:
                return k