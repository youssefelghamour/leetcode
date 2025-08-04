class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        # Hashtable representing the baskets (must only have 2 pairs, 2 baskets)
        # keys: the type of fruit/tree
        # values: the number of fruits we picked from that tree
        baskets = {}
        l = 0
        # The max number of fruits we picked with at most 2 types (the size of the window with only 2 types)
        max_fruits = 0

        for r in range(len(fruits)):
            fruit = fruits[r]
            
            # Add the fruit to the basket (or increase its count)
            if fruit not in baskets:
                baskets[fruit] = 0
            baskets[fruit] += 1

            # While we have more than 2 fruit types, shrink from the left
            while len(baskets) > 2:
                left_fruit = fruits[l]

                # Since the leftmost fruit has been removed from the window we have to decrease its count
                baskets[left_fruit] -= 1

                # If we took all of that fruit out, remove its type
                if baskets[left_fruit] == 0:
                    del baskets[left_fruit]

                # Shrink the window
                l += 1

            # r - l + 1 is the size of the window (1 to account for r)
            # Keep track of the biggest window seen so far with the most fruits from only 2 types
            max_fruits = max(max_fruits, r - l + 1)

        return max_fruits