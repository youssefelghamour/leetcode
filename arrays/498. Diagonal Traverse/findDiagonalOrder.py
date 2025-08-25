class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        m = len(mat)
        n = len(mat[0])
        i,j = 0,0
        up = True
        result = []

        while len(result) < m * n:
            result.append(mat[i][j])

            if up:
                if j == n - 1:  # Last element in the row -> go below it (3 to 6)
                    i += 1
                    up = False  # can't go right on last col
                elif i == 0:  # Mid element in the row -> Go to the right of it (1 to 2)
                    j += 1
                    up = False  # can't go up from first row
                else:  # Inside the diagonal -> go to next diagonal element: up right (7 to 5)
                    i -= 1
                    j += 1
            else:
                if i == m - 1:  # Last element in the col -> go to the right of it (8 to 9)
                    j += 1
                    up = True  # can't go below on last row
                elif j == 0:  # Mid element in the col -> Go below it (4 to 7)
                    i += 1
                    up = True  # can't go left o, first col
                else:  # Inside the diagonal -> go to next diagonal element: below left (6 to 8)
                    i += 1
                    j -= 1

        return result