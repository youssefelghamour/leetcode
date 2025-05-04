"""class Solution:
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
"""
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int

        At a certain step `c`, we either came from the step right before it `b` by taking 1 step,
        or the step before that `a` by taking two steps
        the number of ways to reach step `c` would be the number of ways we needed to reach `a` + the
        number of ways we needed to reach `b`
                            ...
                        _c_|
                    _b_|
                _a_|
            ...|
        dp list will hold the number of unique ways to reach every step:
            - 0: ground: dp[0] = 1 way to be at step 0 is to start there
            - 1: dp[1] = 1 way to reach step 1, from step 0
            - 2: dp[2] = dp[1] + dp[0] = 1 + 1 = 2 ways (1->2 in 1 step or 0->2 in 2 steps)
            - 3: dp[3] = dp[2] + dp[1] = 1 + 2 = 3
            ...
        """
        dp = [1 for _ in range(n + 1)]

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[-1]