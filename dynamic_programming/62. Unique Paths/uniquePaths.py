class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Each element in the matrix represents the number of unique paths to that cell
        result = [[0] * n for _ in range(m)]
        
        # There's only one way to reach the first cell (0,0): starting there
        result[0][0] = 1
        # For the first column there's only one way to reach each cell: move down
        for i in range(1, m):
            result[i][0] = 1  
        # For the first row there's only one way to reach each cell: move right
        for j in range(1, n):
            result[0][j] = 1
                
        """ For every cell, the number of ways to reach it is the sum of the
            ways to reach the cell above it and the cell to the left of it
            because we can either move down or to the right
        """
        for i in range(1, m):
            for j in range(1, n):
                result[i][j] = result[i][j - 1] + result[i - 1][j]
        print(result)
        # The bottom right corner cell contains the number of all the unique paths to reach it
        return result[m-1][n-1]