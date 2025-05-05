class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # Update the values of the list: each step contains the minimum cost to reach it
        for i in range(2, len(cost)):
            # We either came from the prev step or the one before it
            # We choose the one having the minimum sum cost
            cost[i] += min(cost[i-1], cost[i-2])
        
        # We reach the end (len(cost)), by either taking 2 steps from -2, or 1 step from last step -1
        return min(cost[-1], cost[-2])