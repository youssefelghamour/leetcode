class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        result = []
        
        for i in range(len(boxes)):
            nb_operations = 0
            for j in range(len(boxes)):
                if boxes[j] == "1":
                    nb_operations += abs(i - j)
            result.append(nb_operations)
        
        return result