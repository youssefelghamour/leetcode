class Solution(object): 
    def __init__(self):
        """ Use meoization to store already computed sub expressions
            memo = { "subexpression": [its result] }
        """
        self.memo = {}


    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]

        1. Find operator '*' at index 1:
            - Left: "2" -> return [2]
            - Right: "3-4*5" -> 
                - Check memo for "3-4*5" -> not found, so compute recursively:
                    - '-' at index 1:
                        - Left: "3" -> return [3]
                        - Right: "4*5" -> 
                            - Check memo for "4*5" -> not found, compute recursively:
                                - '*' at index 1:
                                    - Left: "4" -> return [4]
                                    - Right: "5" -> return [5]
                                    - Combine: 4 * 5 = 20
                                    - Memoize: "4*5" -> [20]
                            - Combine: 3 - 20 = -17
                            - result.append(-17)
                    - '*' at index 3:
                        - Left: "3-4" -> 
                            - Check memo for "3-4" -> not found, compute recursively:
                                - '-' at index 1:
                                    - Left: "3" -> return [3]
                                    - Right: "4" -> return [4]
                                    - Combine: 3 - 4 = -1
                                    - Memoize: "3-4" -> [-1]
                        - Right: "5" -> return [5]
                        - Combine: -1 * 5 = -5
                        - result.append(-5)
                - Memoize: "3-4*5" -> [-17, -5]
                - Combine: 2 * (-17) = -34 and 2 * (-5) = -10
            - result for first iteration = [-34, -10]
        ...
        """
        result = []

        # If the expression is just a number, return it as a list with that single integer
        if expression.isdigit():
            return [int(expression)]
        
        # Check if the result is cached
        if expression in self.memo:
            return self.memo[expression]

        for i in range(len(expression)):
            # If the current character is an operator
            if expression[i] in '+-*':
                # Recursively calculate the results for the left and right expressions
                left_result = self.diffWaysToCompute(expression[:i])
                right_results = self.diffWaysToCompute(expression[i+1:])

                # Combine the results of left and right parts based on the operator
                for l in left_result:
                    for r in right_results:
                        if expression[i] == '+':
                            result.append(l + r)
                        elif expression[i] == '-':
                            result.append(l - r)
                        elif expression[i] == '*':
                            result.append(l * r)

        # Store the result of this subexpression so we don't calculate it again
        self.memo[expression] = result

        return result