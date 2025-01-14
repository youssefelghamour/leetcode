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
        """
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
                ""
                    ex: digits = "23", 2nd loop: digit = 3, result = ['a', 'b', 'c'], letters = ['d', 'e', 'f']
                    - combination 'a': temp = ['ad', 'ae', 'af']
                    - combination 'b': temp = ['ad', 'ae', 'af', 'bd','be','bf']
                        ...
                    -> result = temp = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
                ""
                for combination in result:
                    # For each existing combination, combine it with each letter
                    for letter in letters:
                        # Add the new combination to the list
                        temp.append(combination + letter)
                # Update result with the new combinations
                result = temp
        """
        # Backtracking approach: DFS
        """
            ex: digits = "23"
            (Start)
            i = 0, digits[0] = '2', digit_letters[digits[i]] = ['a', 'b', 'c']                  <- first level
                |
                └── sol = ['a'] (Choose 'a' from '2')
                    |
                    i = 1, digits[1] = '3', digit_letters[digits[i]] = ['d', 'e', 'f']          <- second level
                    |   |
                    |   ├── sol = ['a', 'd'], Append 'd'
                    |   |   |
                    |   |   i = 2, (result = ['ad'])                                            <- third level
                    |   |   |
                    |   |   Remove last element sol.pop() and move to the next letter 'e'
                    |   |
                    |   ├── sol = ['a', 'e'], Append 'e'
                    |   |   |
                    |   |   i = 2, (result = ['ad', 'ae'])
                    |   |   |
                    |   |   Remove last element sol.pop() and move to the next letter 'f'
                    |   |
                    |   └── sol = ['a', 'f'], Append 'f'
                    |       |
                    |       i = 2, (result = ['ad', 'ae', 'af'])
                    |       |
                    |       Remove last element sol.pop()
                    |
                    Remove last element 'a' sol.pop() and move to the next letter 'b'
        """

        result, sol = [], []
        n = len(digits)

        if digits == '':
            return []

        def backtrack(i=0):
            # If we've processed all digits, the current combination is complete
            if i == n:
                # Combine the current letters in sol to form a string: ex: 'aeh'
                result.append(''.join(sol))
                return
            
            # Explore all letters for the current digit
            for letter in digit_letters[digits[i]]:
                sol.append(letter)  # Choose a letter and add it to the current combination
                backtrack(i+1)      # Move to the next digit and recursively build the next level of combinations
                sol.pop()           # Remove the last letter to explore the next letter
        
        # Start backtracking from the first digit
        backtrack(0)
        
        return result