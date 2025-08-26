class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        """
        :type dimensions: List[List[int]]
        :rtype: int
        """
        longest_diag = 0
        max_area = 0

        for l, w in dimensions:
            diagonal = sqrt(l*l + w*w)
            area = l * w

            if diagonal > longest_diag or (diagonal == longest_diag and area > max_area):
                longest_diag = diagonal
                max_area = area
        
        return max_area