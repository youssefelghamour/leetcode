class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # Morse mapping for alphabet letters a-z in lower case
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        # To store unique transformations
        transformations = set()
        
        for word in words:
            transf = ""
            for char in word:
                # ord(char): gets the ASCII, -97 to make it 0 indexed so we can map it to morse
                transf += morse[ord(char) - 97]
            transformations.add(transf)
        
        return len(transformations)