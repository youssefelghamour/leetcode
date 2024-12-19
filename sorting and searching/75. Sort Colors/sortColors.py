class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = ones = twos = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            if nums[i] == 1:
                ones += 1
            if nums[i] == 2:
                twos += 1
        
        nums[:zeros] = [0] * zeros
        nums[zeros:zeros + ones] = [1] * ones
        nums[zeros + ones:] = [2] * twos
        
        return nums