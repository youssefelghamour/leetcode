class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        first_row = "qwertyuiop"
        second_row = "asdfghjkl"
        third_row = "zxcvbnm"

        for word in words:
            lowercase_word = word.lower()
            if (all(char in first_row for char in lowercase_word) or
                    all(char in second_row for char in lowercase_word) or
                    all(char in third_row for char in lowercase_word)):
                result.append(word)
        
        return result