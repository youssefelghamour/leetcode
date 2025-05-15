class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        # dictionary to map letters in pattern to words in s
        d = {}
        # split the string into words
        words = s.split(" ")

        if len(pattern) != len(words):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] in d:
                # if the letter in the dictionary is mapped to a different word
                if d[pattern[i]] != words[i]:
                    return False
            else:
                # if the word is already used for another letter
                if words[i] in d.values():                   
                    return False
                d[pattern[i]] = words[i]
        
        return True