class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        lp_dict = {}
        completing_words = []

        # Remove spaces
        licensePlate = licensePlate.lower().replace(" ", "")
        # Remove numbers
        for char in licensePlate:
            if char.isdigit():
                licensePlate = licensePlate.replace(char, "")

        # Make a dictionary of characters from licensePlate as keys and their occurence as values
        for char in licensePlate:
            if char in lp_dict:
                lp_dict[char] += 1
            else:
                lp_dict[char] = 1
        
        for word in words:
            word_dict = {}
            # Make a dictionary of chars from the word as keys and their occurence as values
            for char in word:
                if char in word_dict:
                    word_dict[char] += 1
                else:
                    word_dict[char] = 1
            
            """
            flag = True
            for key, value in lp_dict.items():
                if key not in word_dict or word_dict[key] < value:
                    flag = False
                    break
            """
            # If all characters from licensePlate exist in the word with at least the same occurence
            if all(lp_dict[key] <= word_dict.get(key, 0) for key in lp_dict.keys()):
                completing_words.append(word)
        
        # Start with the first word
        shortest_word = completing_words[0]
        for word in completing_words:
            # If there's a shorter word
            if len(word) < len(shortest_word):
                shortest_word = word
        
        return shortest_word