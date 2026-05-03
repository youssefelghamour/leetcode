class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        # Array storing [in-degree, out-degree] for every node i: 1 to n
        # Ignore index 0 with a placeholder as it's not a node
        trust_count = [[0,0] for _ in range(n+1)]

        for rel in trust:
            out_node = rel[0]
            in_node = rel[1]

            trust_count[out_node][1] += 1
            trust_count[in_node][0] += 1
        
        # If a node exists with out-degree 0 and in-degree = n-1 return its index
        for i in range(1,len(trust_count)):
            if trust_count[i][0] == n -1 and trust_count[i][1] == 0:
                return i

        return -1
