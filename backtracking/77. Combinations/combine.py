class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        stack = []

        def backtrack(start):
            if len(stack) == k:
                result.append(stack[:])
                return
            
            for i in range(start, n + 1):
                stack.append(i)
                backtrack(i + 1)
                stack.pop()
        
        backtrack(1)

        return result