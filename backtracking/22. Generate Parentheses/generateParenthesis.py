class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        # Stack includes each combination at a time
        stack = []
        
        # When backtracking, the function always goes back until it reaches the
        # last opening parenthesis  and pops it, then explores other paths from there
        def backtrack(open, closed):
            """
                The function adds an opening parenthesis first,
                it then tries all valid paths by adding closing parentheses.
                Once a path is fully explored, it pops the last opening parenthesis
                to backtrack and try a different combination.
            """
            # If n opening and n closing parentheses have been added
            if open == n and closed == n:
                # Turn the stack containing the combination into a string and add it to result
                result.append("".join(stack))
                return
            
            # We add an opening parenthese first, because we can't close it if we start with a closing one
            if open < n:
                stack.append("(")
                backtrack(open + 1, closed)
                stack.pop()
            
            # We can only add closing parentheses if there are more open ones (not closed)
            # That way we ensure we close all of the already open parentheses
            if closed < open:
                stack.append(")")
                backtrack(open, closed + 1)
                stack.pop()
        
        
        # Start the process with 0 open and closed parentheses
        backtrack(0,0)
        
        return result