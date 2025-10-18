class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        """
        No need to calculate the average
        left = 0
        right = k
        current_sum = sum(nums[left:right])  # first window
        # float(k) because dividing two integers drops the decimal (12.75 becomes 12.00)
        max_average = current_sum / float(k)

        while right < len(nums):
            current_sum = current_sum - nums[left] + nums[right]
            left += 1
            right += 1
            max_average = max(max_average, current_sum / float(k))

        return max_average
        """
        current_sum = sum(nums[0:k])  # first window
        max_sum = current_sum

        for right in range(k, len(nums)):
            current_sum = current_sum - nums[right - k] + nums[right]
            max_sum = max(max_sum, current_sum)

        return max_sum / float(k)