class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool

        Two strings are close:
        1. If they have the same length
        2. Made up of the same letters
        3. The occurrences of characters must be equal in both strings
            but since operation 2 allows us to transform characters
            if word1 has 1 b & 2 c, while word2 has 2 b & 1 c
            we can turn word1 into word2
            comparing occurrence in this case is wrong
            we should compare the sorted lists made of the occurrences
            word1: [1,2], word2: [2, 1] -> [1, 2]
        """
        if len(word1) != len(word2):
            return False
        
        # Dicts to map each character to the number of its occurrence
        occ1 = {}
        occ2 = {}

        for char in word1:
            occ1[char] = occ1.get(char, 0) + 1
        
        for char in word2:
            occ2[char] = occ2.get(char, 0) + 1

        # Make sure the two strings are made of the same characters
        # And have the same sorted occurence list
        return set(occ1.keys()) == set(occ2.keys()) and sorted(occ1.values()) == sorted(occ2.values())