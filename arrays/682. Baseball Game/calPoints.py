class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        records = []

        for x in operations:
            if x == '+':
                records.append(sum(records[-2:]))
            elif x == 'D':
                records.append(records[-1] * 2)
            elif x == 'C':
                records.pop()
            else:
                records.append(int(x))
        
        return sum(records)