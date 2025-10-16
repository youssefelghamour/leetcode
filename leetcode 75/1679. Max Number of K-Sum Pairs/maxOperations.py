class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        count = 0

        nums.sort()

        while left < right:
            if nums[left] + nums[right] == k:
                left += 1
                right -= 1
                count += 1
            elif nums[left] + nums[right] < k:
                left += 1
            else:
                right -= 1
        
        return count