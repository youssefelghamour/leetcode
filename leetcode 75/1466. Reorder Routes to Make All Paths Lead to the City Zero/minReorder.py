class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int

        - Create an adjacency list
        - Turn the graph into a bidirectional graph (if a -> b add b -> a)
            - Store direction info in the adjacency list to keep track of reversed directions
        - Traverse the graph starting from vertex 0 with DFS
            - If the connections has been reversed increase the count of reversed edges
        """
        # Key: vertex, Value: a set (neighbor, is_original_direction)
        # is_original_direction is True if vertex -> neighbor in connections
        graph = {}
        count = 0
        stack = []
        visited = set()

        # DFS to create the adjacency list
        for connection in connections:
            a = connection[0]
            b = connection[1]

            graph.setdefault(a, []).append((b, True))  # Original direction
            graph.setdefault(b, []).append((a, False))  # Reversed
        
        stack.append(0)
        visited.add(0)

        while stack:
            current = stack.pop()

            for neighbor, is_original_direction in graph[current]:
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)

                    # Check if the edge has been reversed
                    # Since we're trying to make neighbor -> current
                    # If the original was current -> neighbor then it's a reversed edge
                    """
                    for conn in connections:
                        if conn[0] == current and conn[1] == neighbor:
                    """
                    if is_original_direction:
                            count += 1
        
        return count