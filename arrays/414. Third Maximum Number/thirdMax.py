class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        first_max = max(nums)
        # Remove all occurences of the first max
        while first_max in nums:
            nums.remove(first_max)
        # If the list is empty (no third max), return the first max
        if not nums:
            return first_max
        
        second_max = max(nums)
        # Remove all occurences of the second max
        while second_max in nums:
            nums.remove(second_max)
        # If the list is empty (no third max), return the first max
        if not nums:
            return first_max
        
        third_max = max(nums)
        
        return third_max
        """
        # Turn into a set to remove duplicates
        nums = list(set(nums))

        # If there's no third max
        if len(nums) < 3:
            # Return the first max
            return max(nums)
            
        nums.sort()
        return nums[-3]