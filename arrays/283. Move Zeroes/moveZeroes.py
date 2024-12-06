class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Track where to put non zero elements
        index = 0
        
        # This sorts the array putting non zero numbers at the beginning
        # leaving zeros at the end
        for i in range(len(nums)):
            if nums[i] != 0:
                temp = nums[index]
                nums[index] = nums[i]
                nums[i] = temp
                index += 1