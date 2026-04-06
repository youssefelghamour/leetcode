class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """ O(n) time complexity but two dicts make it O(n) space complexity
        # Dictionary for all left sums for each index
        left_sum = {}
        # Dictionary for all right sums for each index
        right_sum = {}

        # No sum left of first element, and no sum right of last element
        left_sum[0] = 0
        right_sum[len(nums) - 1] = 0

        sum = 0
        # Calculate left sums
        for i in range(1, len(nums)):
            # Accumulate the sum
            sum += nums[i -1]
            left_sum[i] = sum

        # Reset sum to 0
        sum = 0
        # Calculate right sums
        for i in range(len(nums) - 2, -1, -1):
            sum += nums[i + 1]
            right_sum[i] = sum
        
        # Compare left and right sums for each index
        for k in range(len(nums)):
            # If a pivot is found where left sum = right sum, return it
            if left_sum[k] == right_sum[k]:
                return k
        
        return -1
        """
        total_sum = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            # Calculate the right sum for each iteration
            right_sum = total_sum - left_sum - nums[i]

            if left_sum == right_sum:
                return i
            
            # Update the value of left_sum
            left_sum += nums[i]

        return -1