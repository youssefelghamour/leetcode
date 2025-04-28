class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        s = float('inf') # Set the initial sum far from the target so the first check fails

        # Sorting allows us to move the left pointer forward to increase the sum,
        # and the right pointer backward to decrease the sum
        nums.sort()

        # For every nums[i], check the rest of the array [i+1, ...]
        for i in range(0, len(nums) - 2): # - 2 accounts for the window (left & right)
            # Use a sliding windown to check the rest of the arr [left, ..., right]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]

                if abs(curr_sum - target) < abs(s - target):
                    # If the current window's sum is closer to target than the prev sum
                    s = curr_sum
                
                if curr_sum < target:
                    # If the current sum is less than target, increase it by moving left forward
                    left += 1
                else:
                    # If the current sum is more than target, decrease it by moving right backward
                    right -= 1
        
        return s