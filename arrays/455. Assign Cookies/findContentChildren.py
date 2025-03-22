class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        i, j = 0, 0
        count = 0

        # For every child (i) we keep checking until we find a cookie (j)
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                count += 1
                i += 1 # This child has a cookie now, go to the next child
            j += 1

        return count