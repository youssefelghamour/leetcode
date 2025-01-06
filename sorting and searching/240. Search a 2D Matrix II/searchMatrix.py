from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Number of rows
        m = len(matrix)
        # Number of columns
        n = len(matrix[0])
        
        # Start from the top right corner: last element of a row which is the max of that row
        row = 0
        column = n - 1
        
        while row < m and column >= 0:
            if matrix[row][column] == target:
                return True
            # If the current value in the row is smaller than target, move down
            # Because the rows are sorted, the next row might have a larger value
            elif matrix[row][column] < target:
                row += 1
            # If the current value is larger than target, move left
            # Because the columns are sorted, the previous column might have a smaller value
            else:
                column -= 1
        
        return False