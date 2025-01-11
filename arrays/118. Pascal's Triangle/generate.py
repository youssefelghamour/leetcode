class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        
        triangle.append([1])
        
        for i in range(1, numRows):
            prev_row = triangle[i-1]
            row = []
            
            row.append(1)
            for j in range(1, i):
                row.append(prev_row[j] + prev_row[j - 1])
            row.append(1)
            
            triangle.append(row)
            
        return triangle