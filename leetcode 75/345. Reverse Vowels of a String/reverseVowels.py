class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        l = 0
        r = len(s) - 1
        s = list(s)

        while l < r:
            if s[l] in vowels and s[r] in vowels:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            else:
                if s[l] not in vowels:
                    l += 1
                if s[r] not in vowels:
                    r -= 1
        
        return ''.join(s)