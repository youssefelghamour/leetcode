class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_letters = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
        result = []
        
        for digit in digits:
            # The letters for the current digit
            letters = digit_letters[digit]

            # If result is empty, it means we are processing the first digit
            if not result:
                result = letters
            # Combine the current letters with the existing combinations in the result
            else:
                # Temp list to hold the new combinations
                temp = []
                # Combine each combination in result with every letter from the current digit's letters
                """
                    ex: digits = "23", 2nd loop: digit = 3, result = ['a', 'b', 'c'], letters = ['d', 'e', 'f']
                    - combination 'a': temp = ['ad', 'ae', 'af']
                    - combination 'b': temp = ['ad', 'ae', 'af', 'bd','be','bf']
                        ...
                    -> result = temp = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
                """
                for combination in result:
                    # For each existing combination, combine it with each letter
                    for letter in letters:
                        # Add the new combination to the list
                        temp.append(combination + letter)
                # Update result with the new combinations
                result = temp
        
        return result