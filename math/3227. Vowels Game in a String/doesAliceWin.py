class Solution(object):
    def doesAliceWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels = {'a', 'e', 'i', 'o', 'u'}

        for c in s:
            if c in vowels:
                # Alice always wins if there's at least one vowel
                return True
        
        return False