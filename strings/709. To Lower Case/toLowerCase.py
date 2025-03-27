class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        for c in s:
            if 65 <= ord(c) <= 90:
                result += chr(ord(c) + 32)
            else:
                result += c
        return result