class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        lst = []
        
        for num in nums:
            if nums.count(num) == 1:
                lst.append(num)
        
        return lst