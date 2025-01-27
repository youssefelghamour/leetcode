class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def pow(x, n):
            r = 1
            for i in range(1, n+1):
                r *= x
            return r
        
        if n > 0:
            return pow(x, n)
        elif n < 0:
            if x == 0:
                return 0
            else:
                return pow(1/x, abs(n))
        if n == 0:
            return 1