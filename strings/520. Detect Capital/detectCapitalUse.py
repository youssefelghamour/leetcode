class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) == 1:
            return True
        
        # If all upper case
        if all(ord('A') <= ord(char) <= ord('Z') for char in word):
            return True
        
        # If all lower case
        if all(ord('a') <= ord(char) <= ord('z') for char in word):
            return True
        
        # If the first letter is uppercase and the rest are lowercase
        if ord('A') <= ord(word[0]) <= ord('Z') and all(ord(char) >= 97 and ord(char) <= 122 for char in word[1:]):
            return True
        
        return False
            