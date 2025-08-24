class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        zeros_count = 0
        result = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros_count += 1
            
            # Window has more than 1 zero: shrink from left to remove the prev 0
            while zeros_count > 1:
                if nums[left] == 0:
                    zeros_count -= 1
                left += 1
            
            # Length after deleting one element = window size - 1
            result = max(result, right - left)
        
        return result