class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]

        the nodes are the indices, and each index in graph has a list of where the curr node (index) can go to
        make a path from every element and then bakctrack and choose another element
        ex: graph = [[1,2],[3],[3],[]]
            - node 0: we can go to node 1 or 2 - stack = [0]
                - 0 -> 1: stack.append(graph[0][0]) = [0, 1] go to graph[1] = [3] ( backtrack(neighbor) )
                    - 0 -> 1 -> 3: stack = [0, 1, 3] go to graph[3] = [] ( bakctrack -> node = 3 = len - 1)
                        we reached the end (nowhere to go from here) result.append([0, 1, 3])
        """
        stack = [0]  # Start from 0
        result = []

        def backtrack(node):
            # We reached the edge (nowhere to go from here)
            if node == len(graph) - 1:
                result.append(stack[:])
                return
            
            for neighbor in graph[node]:
                # Choose a path
                stack.append(neighbor)
                # Go to that node we chose from the sublist
                backtrack(neighbor)
                stack.pop()
            
        backtrack(0)

        return result