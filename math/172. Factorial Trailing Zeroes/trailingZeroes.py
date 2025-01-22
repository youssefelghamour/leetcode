class Solution:
    def trailingZeroes(self, n: int) -> int:
        zeros = 0
        f = 1
        
        if n == 0 or n == 1:
            return 0
        
        while n != 1:
            f *= n
            n -= 1
        
        while f > 0 and f % 10 == 0:
            zeros += 1
            f //= 10
        
        return zeros