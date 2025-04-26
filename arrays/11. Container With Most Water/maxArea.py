class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        amount = 0
        i, j = 0, len(height) - 1

        while i < j:
            tmp_amount = min(height[i], height[j]) * (j - i)
            # Keep track of the biggest amount
            amount = max(amount, tmp_amount)

            # Move the pointer with the smaller height
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        
        return amount