class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        i = 0
        length = len(flowerbed)

        """
        # Handle list with one element
        if (len(flowerbed) == 1 and flowerbed[0] == 0):
            return True

        while i < len(flowerbed):
            if (flowerbed[i] == 1):
                i += 2
                continue

            # Handle the last element
            if (i == len(flowerbed) - 1 and len(flowerbed) > 1 and flowerbed[len(flowerbed) - 2] == 0):
                n -= 1  # Plant a flower
                i += 1  # Skip next plot
                continue

            # Hanlde first and middle elements
            if (i > 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0) or (i == 0 and len(flowerbed) > 1 and flowerbed[1] == 0):
                n -= 1
                i += 2
            else:
                i += 1
        """

        while i < length:
            # Check if current spot is empty and both neighbors are empty or out of bounds
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == length-1 or flowerbed[i+1] == 0):
                n -= 1  # Plant a flower
                i += 2  # Skip next plot
            else:
                i += 1  # Move to next plot

        # Check exact or overplanted plants
        return n <= 0