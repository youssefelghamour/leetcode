class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead

        Do not check for zeros — removing and adding them at the end causes an infinite loop
        Use two-pointer swap: check for non-zero elements and move them to the start
            1. Loop index scans for non-zeros
            2. Other index starts at 0, tracking where to place non-zeros
            3. If element at i is non-zero, swap it with element at index (element at index is always zero)
        """
        index = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[index], nums[i] = nums[i], nums[index]
                index += 1
        
        return nums