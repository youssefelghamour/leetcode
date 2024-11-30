class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        min = prices[0]
        
        for i in range(1, len(prices)):
            # update min if we found a new minimum
            if prices[i] < min:
                min = prices[i] 
            
            # check if the difference is greater than the previous profit
            temp = prices[i] - min
            if temp > profit:
                profit = temp
        
        return profit