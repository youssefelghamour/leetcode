from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        queue = deque()
        visited = set()
        minutes = 0
        m = len(grid)
        n = len(grid[0])
        fresh = 0

        # Find all rotten nodes and add them to the queue
        # This will start BFS on these nodes simultaneously simulating
        # a simultaneous spread at the same time from different sources
        found = False
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    found = True
                    # Count all fresh nodes to see if any remains at the end
                    fresh += 1
        
        # No fresh oranges
        if not found:
            return 0

        # Number of node in the current level
        current_level = len(queue)
        # BFS
        while queue:
            node = queue.popleft()
            i, j = node
            current_level -= 1  # Current vertex processed

            # Upper
            if i - 1 >= 0 and grid[i-1][j] == 1:
                if (i-1, j) not in visited:
                    queue.append((i-1, j))
                    visited.add((i-1, j))
                    grid[i-1][j] = 2
                    fresh -= 1

            # Bottom
            if i + 1 < m and grid[i+1][j] == 1:
                if (i+1, j) not in visited:
                    queue.append((i+1, j))
                    visited.add((i+1, j))
                    grid[i+1][j] = 2
                    fresh -= 1

            # Left
            if j - 1 >= 0 and grid[i][j-1] == 1:
                if (i, j-1) not in visited:
                    queue.append((i, j-1))
                    visited.add((i, j-1))
                    grid[i][j-1] = 2
                    fresh -= 1

            # Right
            if j + 1 < n and grid[i][j+1] == 1:
                if (i, j+1) not in visited:
                    queue.append((i, j+1))
                    visited.add((i, j+1))
                    grid[i][j+1] = 2
                    fresh -= 1
            
            if current_level == 0:
                # Start a new BFS layer
                # queue now holds all the neighbors of the previous layer's rotten nodes
                current_level = len(queue)
                # Prevent adding a min after processing the last layer (it produces no new rot)
                if current_level != 0:
                    # Each BFS layer is one minute
                    minutes += 1
        
        # If after the whole spread an unreachable fresh node still exists
        if fresh > 0:
            return -1
        
        return minutes