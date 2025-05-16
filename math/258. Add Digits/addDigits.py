class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            tmp = 0
            for d in str(num):
                tmp += int(d)
            num = tmp
        return num