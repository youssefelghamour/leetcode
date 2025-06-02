class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0

        for i in range(1, len(s)):
            sum += abs(ord(s[i - 1]) - ord(s[i]))
        
        return sum