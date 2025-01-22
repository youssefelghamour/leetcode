class Solution:
    def trailingZeroes(self, n: int) -> int:
        """
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
        """
        """
            Counts how many times 5 appears in the factors from 1 to n.
            Because every time 5 multiplies by 2, we get a trailing zero (5 * 2 = 10).

            In the range from 1 to n:
                - First, count how many numbers are divisible by 5. 
                - Then count how many are divisible by 25 (since 25 = 5 * 5 adds an extra 5).
                - Then count how many are divisible by 125 (since 125 = 5 * 5 * 5 adds another 5).
                ...
            We continue this process until the number is bigger than n.

            Formula:
                zeros = (n // 5) + (n // 25) + (n // 125) + ...
                zeros = (n // 5**1) + (n // 5**2) + (n // 5**3) + ...

            Example:
                For 10! = 10 × 9 × 8 × 7 × 6 × 5 × 4 × 3 × 2 × 1 = 100:
                    - 5 is in 5, and 10 (5x2), so we count 2 (10 // 5 = 2)
                    - No numbers with 25 or 125, so we stop here. (for i=2: 5**2 = 25 > n)
                So 10! has 2 trailing zeros.
        """
        zeros = 0
        
        i = 1
        while 5**i <= n:
            zeros += n // (5**i) 
            i += 1
        
        return zeros