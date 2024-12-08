class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        
        for i in range(n):
            for j in range(n):
                if board[i][j] == '.':
                    continue
                    
                for k in range(n):
                    # Check row
                    if k != j and board[i][j] == board[i][k]:
                        return False
                    
                    # Check column
                    if k != i and board[i][j] == board[k][j]:
                        return False
                
                # Get duplicate in 3x3 subgrid
                # (i or j // 3) gives the index of the 3x3 subgrid row/column
                # Dividing by 3 maps rows 0-2 to 0, rows 3-5 to 1, rows 6-8 to 2
                box_row = i // 3 # Get subgrid row
                box_column = j // 3 # Get subgrid column
                
                # Check 3x3 box
                for l in range(3):
                    for m in range(3):
                        
                        # box_row * 3 gives the start of the 3x3 block, l adds the offset
                        row = box_row * 3 + l
                        # box_column * 3 gives the start of the 3x3 block, m adds the offset
                        col = box_column * 3 + m
                        
                        if (row != i or col != j) and board[i][j] == board[row][col]:
                            return False
                
        return True