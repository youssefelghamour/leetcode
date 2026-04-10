class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        
        """
        # Compare every row to all columns
        for i in range(len(grid)):
            row = grid[i]
            col = []
            for j in range(len(row)):
                # Construct the jth column (jth elemnt from every k line)
                for k in range(len(grid)):
                    col.append(grid[k][j])
                # Compare col and row
                if row == col:
                    print(col)
                    result += 1
                # Check the next colum
                col = []
        """
        rows = grid
        columns = []

        # Columns
        for j in range(len(grid[0])):
            col = []
            # Rows
            for i in range(len(grid)):
                col.append(grid[i][j])
            columns.append(col)
        
        for row in rows:
            for col in columns:
                if row == col:
                    result +=1

        return result