from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        # The index of the letter we're checking from the word
        index = 0
        
        
        def dfs_check_word(i, j, index):
            """ Recursively checks if the word can be formed starting from the given cell.
                If the character matches the letter at index, it continues to check adjacent cells.
            """
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] == '#' or board[i][j] != word[index]:
                return False
            # If the last character is matched (board[i][j] = word[len(word) - 1])
            if index == len(word) - 1:
                # return True, the whole word is found
                return True
            
            # Save the value of the current cell
            temp = board[i][j]
            # Mark the current cell as visited by replacing it with '#'
            board[i][j] = '#'
            
            # Recur for all four directions (right, down, left, up)
            # True if one direction finds the word
            found = ( dfs_check_word(i, j+1, index+1) or 
                      dfs_check_word(i+1, j, index+1) or
                      dfs_check_word(i, j-1, index+1) or
                      dfs_check_word(i-1, j, index+1)
                    )
            
            # Restore the cell's original value after recursion, because we may visit it from another path
            board[i][j] = temp
            
            # Return True if the word is found, otherwise False
            return found
        
        
        for i in range(m):
            for j in range(n):
                # Check if the current cell matches the first character of the word
                # If it matches, we can start the recursive search STARTING from this position and checking all paths if they construct the word
                if board[i][j] == word[0]:
                    # If one of the paths from this starting point matches the word, return True
                    if dfs_check_word(i, j, 0) == True:
                        return True
        
        # If no match is found after checking all cells
        return False