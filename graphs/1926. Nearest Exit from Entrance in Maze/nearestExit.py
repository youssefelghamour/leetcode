from collections import deque

class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        queue = deque()
        visited = set()
        result = 0
        # Keep track of how many nodes in each BFS layer
        level_size = 1

        entrance = tuple(entrance)
        queue.append(entrance)
        visited.add(entrance)
        # BFS
        while queue:
            vertex = queue.popleft()
            # Count the current vertex as processed from the current level of BFS
            level_size -= 1
            row = vertex[0]
            col = vertex[1]

            # Check if we've MOVED to the exit
            if (row, col) != entrance:
                if maze[row][col] == '.' and (row == 0 or col == 0 or row == len(maze) - 1 or col == len(maze[0]) - 1):
                    return result

            # Add neighbors to the queue
            if row - 1 >= 0 and maze[row - 1][col] == '.':  # Top
                neighbor = (row - 1, col)
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
            if col - 1 >= 0 and maze[row][col - 1] == '.':  # Left
                neighbor = (row, col - 1)
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
            if col + 1 < len(maze[0]) and maze[row][col + 1] == '.':  # Right
                neighbor = (row, col + 1)
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
            if row + 1 < len(maze) and maze[row + 1][col] == '.':  # Bottom
                neighbor = (row + 1, col)
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

            if level_size == 0:
                # Only increment result for each BFS layer (after visiting all nodes in the current layer)
                result += 1
                level_size = len(queue)

        return -1