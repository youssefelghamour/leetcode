class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # Dictionary to store the most recent index of each number in nums
        d = {}

        for i in range(len(nums)):
            if nums[i] in d and abs(i - d[nums[i]]) <= k:
                return True
            else:
                # Update the value with the most recent index
                d[nums[i]] = i
        
        return False