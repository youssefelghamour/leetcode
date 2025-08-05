class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        for i in range(len(fruits)):
            for j in range(len(baskets)):
                if baskets[j] >= fruits[i]:
                    del baskets[j]
                    break
        
        return len(baskets)