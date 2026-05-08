class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        visited = set()
        graph = {}  # Adjajency list
        stack = []  # DFS

        if not edges:
            # The graph could have nodes that aren't connected
            return source == destination

        for edge in edges:
            a = edge[0]
            b = edge[1]

            if a not in graph:
                graph[a] = []
            graph[a].append(b)

            if b not in graph:
                graph[b] = []
            graph[b].append(a)
        
        stack.append(source)
        while stack:
            current_vertex = stack.pop()
            for neighbor in graph[current_vertex]:
                if neighbor == destination:
                    return True
                if neighbor not in visited:
                    stack.append(neighbor)
                    # Prevent adding the same vertex to the stack before it's popped
                    visited.add(neighbor)

        return False