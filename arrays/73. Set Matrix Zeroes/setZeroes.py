class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        indices = []
        
        for i in range(m):  # row
            for j in range(n):  # column
                if matrix[i][j] == 0:
                    indices.append((i,j))
        
        for ij in indices:
            i,j = ij
            for k in range(n):
                matrix[i][k] = 0
            for k in range(m):
                matrix[k][j] = 0