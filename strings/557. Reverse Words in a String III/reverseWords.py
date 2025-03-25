class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split(' ')
        
        # for word in s
        for i in range(len(s)):
            temp = ""
            # for char in word in reverse
            for j in range(len(s[i]) - 1, -1, -1):
                temp += s[i][j]
            s[i] = temp
        
        return ' '.join(s)