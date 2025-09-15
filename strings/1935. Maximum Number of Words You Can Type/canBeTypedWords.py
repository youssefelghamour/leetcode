class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        result = 0
        brokenLetters = set(brokenLetters)  # Faster lookup
        correct = True  # Not a broken word

        for word in text.split():
            """
            if all(c not in brokenLetters for c in word):
                result += 1
            """
            correct = True

            for c in word:
                if c in brokenLetters:
                    # If only one character is missing
                    correct = False
                    break
            
            if correct:
                result += 1

        return result