class Solution:
    def isHappy(self, n: int) -> bool:
        sum = 0
        # Set to store all the previous sums to check if we've run into a cycle
        seen = set()
        
        seen.add(n)
        
        while sum != 1:
            sum = 0
            
            for d in str(n):
                sum += int(d)**2
                
            if sum == 1:
                return True

            # Check if we're in a cycle
            if sum in seen:
                return False
            
            seen.add(sum)
            n = sum