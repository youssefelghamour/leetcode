class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        
        In a cell, we either came from the left of the top, the path that has the shortest sum,
        so we just need to compare the min of the sums of these cells to know the previous cell we came from

        we make a second matrix to track the min path sum for each cell,
            - The (0,0) cell has the same value as the grid
            - The first row: each cell's sum path is the sum of its prev left cells, we can only come from the left
            - The first col: each cell's sum path is the sum of its prev top cells, we can only come from the top
        """
        """
        # Matrix with min sum path as values for each cell
        sum_matrix = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        sum_matrix[0][0] = grid[0][0]

        # Initialize the first column
        for c in range(1, len(grid[0])):
            sum_matrix[0][c] = grid[0][c] + sum_matrix[0][c-1] # Left cell
        # Initialize the first row
        for r in range(1, len(grid)):
            sum_matrix[r][0] = grid[r][0] + sum_matrix[r-1][0] # top cell
        
        # Fill the rest of the matrix
        for r in range(1, len(grid)):
            for c in range(1, len(grid[0])):
                # Each cell is its actual value + the min path sum of its previous cell we came from (left or top)
                sum_matrix[r][c] = grid[r][c] + min(sum_matrix[r][c-1], sum_matrix[r-1][c])
        
        # Return the value of the bottom right cell that contains now the min path sum leading to it
        return sum_matrix[-1][-1]
        """
        """
        # Updating the matric in place
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                # If cell has top or left (not first cell)
                if r-1 >= 0 or c-1 >= 0:
                    if r-1 < 0:  # If cell doesnt have top
                        # Add left
                        grid[r][c] += grid[r][c-1]
                        continue
                    if c-1 < 0:  # If cell doesnt have left
                        # Add top
                        grid[r][c] += grid[r-1][c]
                        continue
                    else:  # Has both
                        # Add the min path sum between the top and left
                        grid[r][c] += min(grid[r-1][c], grid[r][c-1])
        
        return grid[-1][-1]
        """
        m, n = len(grid), len(grid[0])

        # First row
        for c in range(1,n):
            grid[0][c] += grid[0][c-1]

        # First column
        for r in range(1,m):
            grid[r][0] += grid[r-1][0]

        for r in range(1,m):
            for c in range(1,n):
                grid[r][c] += min(grid[r-1][c], grid[r][c-1])

        return grid[-1][-1]