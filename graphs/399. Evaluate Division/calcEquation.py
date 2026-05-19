class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # Directed weighted adjcaceny list; key: vertex, value: list of neighbors tuples
        # (neighbor, weight of edge a->b)
        graph = {}
        result = []

        for i in range(len(equations)):
            a = equations[i][0]
            b = equations[i][1]

            graph[a] = graph.get(a, [])
            graph[a].append((b, values[i]))

            graph[b] = graph.get(b, [])
            graph[b].append((a, 1 / values[i]))

        for query in queries:
            c = query[0]
            d = query[1]

            if c not in graph or d not in graph:
                result.append(-1)
                continue

            found = False
            answer = -1
            stack = []
            visited = set()
            # Each vertex is added with the cumulative product_so_far for the current path (c -> b -> a)
            # 1 because we're starting at c (c -> c is 1)
            stack.append((c, 1))
            # DFS on the graph
            while stack:
                vertex, product_so_far = stack.pop()

                if vertex in visited:
                    continue

                visited.add(vertex)

                if vertex == d:
                    found = True
                    answer = product_so_far
                    break

                neighbors = graph[vertex]
                for neighbor, weight in neighbors:
                    stack.append((neighbor, product_so_far * weight))
            
            result.append(answer if found else -1)
        
        return result