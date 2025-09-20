class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]

        find the max in the whole array
        The current max stays the max even if we add extra candies, so its value is always true
        For the rest of the elements, we simply check each one against this max
        """
        max_val = max(candies)
        result = []

        for i in range(len(candies)):
            if (candies[i] + extraCandies) >= max_val:
                result.append(True)
            else:
                result.append(False)

        # return [candies[i] + extraCandies >= max_val for i in range(len(candies))]
        return result