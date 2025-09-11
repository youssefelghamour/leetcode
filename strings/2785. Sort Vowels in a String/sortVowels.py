class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str

        Process:
            1. Make a set of vowels (both upper and lower case)
            2. Go through the string once:
                - If char is vowel collect it in a list
                - Also keep track of its index
            3. Sort the list of vowels
            4. Convert the original string into a list (so it’s mutable)
            5. Replace each vowel index (in order) with the next vowel from the sorted list
            6. Turn the list back into a string
        """
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        collected_vowels = []
        indexes = []

        for i in range(len(s)):
            ch = s[i]
            if ch in vowels:
                collected_vowels.append(ch)
                indexes.append(i)
        
        collected_vowels.sort()

        s = list(s)

        j = 0 # Keep track of the vowel replaced from collected_vowels
        # Iterate directly over indexes to replace vowels
        for i in indexes:
            # Replace with the correct vowel
            s[i] = collected_vowels[j]
            j += 1
        
        return "".join(s)