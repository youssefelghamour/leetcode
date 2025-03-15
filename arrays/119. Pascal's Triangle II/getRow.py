class Solution(object):
    def generateTriangle(self, nums_rows):
        """ Generates Pascal's triangle up to the num_rows given """
        triangle = []

        triangle.append([1])

        for i in range(1, nums_rows + 1):
            prev_row = triangle[i - 1]
            curr_row = []

            curr_row.append(1)
            for j in range(1, i):
                curr_row.append(prev_row[j - 1] + prev_row[j])
            curr_row.append(1)

            triangle.append(curr_row)
        
        return triangle        


    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        return self.generateTriangle(rowIndex)[rowIndex]