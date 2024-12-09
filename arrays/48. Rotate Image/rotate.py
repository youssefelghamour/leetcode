class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        for matrix: 
            1  2  3  4
            5  6  7  8
            9  10 11 12
            13 14 15 16
        
        layer 0 would be:
            1  2  3  4
            5        8
            9        12
            13 14 15 16
        
        i = 0 for layer 0:
            1        4
            
            
            13       16
        
        i = 1 for layer 0:
               2      
                     8
            9       
                  15 
        
        layer 1:
               6  7   
               10 11 

        """
        n = len(matrix)
        
        for layer in range(0, n//2):
            for i in range(layer, n - layer - 1):
                # Storing the Top row i'th element
                temp = matrix[layer][i]
                
                
                # Top row i element = Left column i element
                matrix[layer][i] = matrix[n - 1 - i][layer]
                
                # Left column i element = Bottom row i element
                matrix[n - 1 - i][layer] = matrix[n - 1 - layer][n - 1 - i]
                
                # Bottom row i element = Right column i element
                matrix[n - 1 - layer][n - 1 - i] = matrix[i][n - 1 - layer]
                
                # Right column i element = Top row i element
                matrix[i][n - 1 - layer] = temp