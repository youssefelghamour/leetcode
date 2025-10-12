class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0

        if not s:
            return True
        if not t or len(s) > len(t):
            return False

        for i in range(len(t)):
            if t[i] == s[j]:
                j += 1
                if j == len(s):
                    break
        
        return j == len(s)