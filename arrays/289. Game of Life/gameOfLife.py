class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        """
        tmp = []
        tmp = [row[:] for row in board]
        m = len(board)
        n = len(board[0])
        
        
        def check_cell(i,j,val):
            sum = 0
            
            if i > 0:
                sum += board[i-1][j]        # Top
                if j > 0:
                    sum += board[i-1][j-1]  # Top Left
                if j < n-1:
                    sum += board[i-1][j+1]  # Top Right
            
            if i < m-1:
                sum += board[i+1][j]        # Bottom
                if j > 0:
                    sum += board[i+1][j-1]  # Bottom Left
                if j < n-1:
                    sum += board[i+1][j+1]  # Bottom Right
            
            if j > 0:
                sum += board[i][j-1]        # Left
            if j < n-1:
                sum += board[i][j+1]        # Right
            
            if val == 1:
                if sum < 2 or sum > 3:
                    tmp[i][j] = 0
                elif sum == 2 or sum == 3:
                    tmp[i][j] = 1
            elif val == 0 and sum == 3:
                tmp[i][j] = 1
            
        
        for i in range(m):
            for j in range(n):
                check_cell(i,j,board[i][j])
                
        print(board)
        board[:] = tmp
        """
        
        """ 
            Track the modification of the value of the cell, to easily identify the original value
        
            prev      
             val | new | state
            -----+-----+-----
               0 |  0  |  0
               1 |  0  |  1
               0 |  1  |  2
               1 |  1  |  3
        """
        m = len(board)
        n = len(board[0])
        
        
        def prev_val(i,j):
            """ Returns the original value of the updated cell before it was modified """
            if board[i][j] == 2:
                return 0
            if board[i][j] == 3:
                return 1
            else:
                return board[i][j]
        
        
        def sum_neighbours(i,j):
            """ Sums the values of the neighbouring cells: how many cells neighbouring cells are alive
                Only the already processed previous cells have their values updated,
                so we need to get their previous value
            """
            sum = 0
            
            if i > 0:
                sum += prev_val(i-1, j)        # Top
                if j > 0:
                    sum += prev_val(i-1, j-1)  # Top Left
                if j < n-1:
                    sum += prev_val(i-1, j+1)  # Top Right
            
            if i < m-1:
                sum += board[i+1][j]           # Bottom
                if j > 0:
                    sum += board[i+1][j-1]     # Bottom Left
                if j < n-1:
                    sum += board[i+1][j+1]     # Bottom Right
            
            if j > 0:
                sum += prev_val(i, j-1)        # Left
            if j < n-1:
                sum += board[i][j+1]           # Right
                
            return sum
            
            
        for i in range(m):
            for j in range(n):
                sum = sum_neighbours(i,j)
                
                if board[i][j] == 1:
                    if sum < 2 or sum > 3:              # under-population or over-population
                        board[i][j] = 1
                    elif sum == 2 or sum == 3:          # cell stays alive
                        board[i][j] = 3
                elif board[i][j] == 0 and sum == 3:     # reproduction
                    board[i][j] = 2
        
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2 or board[i][j] == 3:
                    board[i][j] = 1
                else:
                    board[i][j] = 0