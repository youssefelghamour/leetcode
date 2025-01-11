class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        m, n = len(grid), len(grid[0])
        
        def bfs_mark_as_water(i, j):
            """ Recursively marks an island as water
                    Gets the indices of the first element of an island,
                    and marks all its adjacent elements so they're not processed twice
            """
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
                return
            else:
                grid[i][j] = '0'
                bfs_mark_as_water(i, j+1)
                bfs_mark_as_water(i+1, j)
                bfs_mark_as_water(i, j-1)
                bfs_mark_as_water(i-1, j)
        
        
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    # Incremenet the count of islands once the first 1 is found
                    num_islands += 1
                    # Mark the adjacent ones as zeros to ignore them so the count of islands isn't incremented again when we visit them
                    bfs_mark_as_water(i, j)
        
        return num_islands