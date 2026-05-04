class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int

        The center of the graph is the node connected to n-1 nodes
        """
        """
        n = len(edges) + 1  # n - 1 edges -> n nodes
        # Ignore index 0, 1 to n nodes
        # List of edges for each node i
        edges_count = [0 for _ in range(n + 1)]

        for i in range(len(edges)):
            a = edges[i][0]
            b = edges[i][1]

            edges_count[a] += 1
            edges_count[b] += 1
        
        return edges_count.index(max(edges_count))
        """
        # Center is connected to all nodes so it apperas in every edge
        a, b = edges[0]
        c, d = edges[1]

        if a == c or a == d:
            return a
        else:
            return b