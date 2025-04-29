class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0] * n for _ in range(n)]
        left = 0
        top = 0
        right = n - 1
        bottom = n - 1
        num = 1

        while left <= right and top <= bottom:
            # Fill top row (left to right)
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            top += 1

            # Fill right column (top to bottom)
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1

            # Fill bottom row (right to left)
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    matrix[bottom][i] = num
                    num += 1
                bottom -= 1

            # Fill left column (bottom to top)
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    matrix[i][left] = num
                    num += 1
                left += 1
        
        return matrix