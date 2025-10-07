class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        
        arrays = [1,   2,  3,  4]
        prefix = [1,   2,  6, 24]
        suffix = [24, 24, 12,  4]

                result[i] = suffix[i-1]    *    prefix[i+1]
                      ___________|__________        ___|__________________
                     |                      |      |                      |
        result[i] = ( result[i+1] * result[i+2] ) * result[i-1] * result[i-2]
                 product of all elements before i * product of all elements after i
        """
        result = [0] * len(nums)
        prefix = nums[:]
        suffix = nums[:]

        # Make the prefix product
        for i in range(1, len(nums)):
            prefix[i] *= prefix[i-1]

        # Make the suffix product
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] *= suffix[i+1]
        
        result[0] = suffix[1]
        result[len(nums) - 1] = prefix[len(nums) - 2]
        for i in range(1, len(nums) - 1):
            result[i] = prefix[i-1] * suffix[i+1]
        
        return result