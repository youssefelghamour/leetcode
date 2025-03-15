class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.split()  # split the string on white spaces = list of words
        return len(s[-1])  # length of the last word