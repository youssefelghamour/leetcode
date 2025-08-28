class Solution(object):
    def sortMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        left_diagonals = []
        right_diagonals = []

        # Construct the diagonals starting from the elements in the first column
        for k in range(len(grid) - 1, -1, -1):
            i = k
            j = 0
            diag = []
            
            while j < len(grid[0]) and i < len(grid):
                diag.append(grid[i][j])
                i += 1
                j += 1
            
            left_diagonals.append(diag)
        
        # Construct the diagonals starting from the elements in the first row
        # We start from 1 because element 0,0's diagonal has been added in the prev loop 
        for k in range(1, len(grid[0])):
            i = 0
            j = k
            diag = []
            
            while j < len(grid[0]) and i < len(grid):
                diag.append(grid[i][j])
                i += 1
                j += 1
            
            right_diagonals.append(diag)
        

        for diag in left_diagonals:
            diag.sort(reverse=True)

        for diag in right_diagonals:
            diag.sort()



        # Reconstructing the matrix from the diagonals we made

        # left diagonals
        for k in range(len(grid) - 1, -1, -1):
            # Traversing the first column from down to top: each element corresponds to the diagonal in left_diag
            i = k
            j = 0
            diag = left_diagonals[0]  # Get the corresponding diagonal
            
            while j < len(grid[0]) and i < len(grid):
                grid[i][j] = diag[0]
                i += 1
                j += 1
                del diag[0]
            
            del left_diagonals[0]  # Remove the diagonal we just processed -> for easy access next loop
        
        # right diagonals
        for k in range(1, len(grid[0])):
            # Traversing the first row from left to right: each element corresponds to the diagonal in right_diag
            i = 0
            j = k
            diag = right_diagonals[0]  # Get the corresponding diagonal
            
            idx = 0
            while j < len(grid[0]) and i < len(grid):
                grid[i][j] = diag[idx]
                i += 1
                j += 1
                idx += 1
            
            del right_diagonals[0]  # Remove the diagonal we just processed -> for easy access next loop

        return grid