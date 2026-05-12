class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int

        Loop over the cities (lines of the matrix)
        For each unvisited city start a DFS to reach all the cities connected to it
        covering the whole province
        While increasing the count of provinces each time we start a new DFS in a province
        """
        visited = set()
        stack = []
        count = 0

        for i in range(len(isConnected)):
            if i not in visited:
                count += 1
                stack = [i]
                visited.add(i)
                while stack:
                    i = stack.pop()
                    i_connections = isConnected[i]
                    for j in range(len(i_connections)):
                        if j not in visited:
                            # If i is connected to j (i_connections[j] == 1)
                            if isConnected[i][j] == 1:
                                # Add connections of j to get all neighbors of j
                                stack.append(j)
                                visited.add(j)
        
        return count
