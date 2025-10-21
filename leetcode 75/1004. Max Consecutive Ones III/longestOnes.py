class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        Go through the array keeping a window of numbers
        Count the zeros in the window because each zero can be flipped to a one
        Whenever the number of zeros is more than k, we move the left forward
        Otherwise we would be trying to flip more zeros than allowed, which is not allowed
        Moving the left removes some zeros and keeps the window valid
        The longest valid window we find this way is the answer

        Approach:
        - Use a sliding window with two pointers: left and right
        - Expand the window by moving right
        - Count the number of zeros in the current window
        - If zeros > k, move left forward until zeros ≤ k
        - Keep track of the maximum window length (right - left + 1)
        """
        left = right = 0
        max_len = 0
        zeros_count = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros_count += 1

            while zeros_count > k:
                # Move left pointer to skip all exceeding zeros on the left
                if nums[left] == 0:
                    zeros_count -= 1
                left += 1

            max_len = max(max_len, right - left + 1)
        
        return max_len