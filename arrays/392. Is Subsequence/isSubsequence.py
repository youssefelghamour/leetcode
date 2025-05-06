class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i, j = 0, 0

        if not s:
            return True
        if not t or len(s) > len(t):
            return False

        while j < len(t):
            if s[i] == t[j]:
                # Found a char of s in t
                i += 1
                
            j += 1

            # Early exit if we find all characters of s
            # Otherwise i will be out of range
            if i == len(s):
                return True

        # Found all chars of s in t?
        return i == len(s)