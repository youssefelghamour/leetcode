class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 2:
            return 2
        elif n == 1:
            return 1
        
        a = 1
        b = 2
        
        for i in range(3, n + 1):
            current = a + b
            a = b
            b = current
        
        return b