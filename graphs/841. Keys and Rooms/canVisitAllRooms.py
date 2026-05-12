class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = set()
        stack = []

        # Start at room 0
        stack.append(0)
        visited.add(0)

        while stack:
            vertex = stack.pop()
            # Get all neighbors of vertex
            for v in rooms[vertex]:
                if v not in visited:
                    stack.append(v)
                    visited.add(v)
        
        # All rooms are open if they have all been visited
        return len(visited) == len(rooms)