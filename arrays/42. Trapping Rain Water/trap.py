class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        amount = 0
        left = 0
        right = len(height) - 1
        left_max_height = height[left]
        right_max_height = height[right]

        while left < right:
            if height[left] < height[right]:
                left_max_height = max(left_max_height, height[left])
                amount += left_max_height - height[left]
                left += 1
            else:
                right_max_height = max(right_max_height, height[right])
                amount += right_max_height - height[right]
                right -= 1
        
        return amount