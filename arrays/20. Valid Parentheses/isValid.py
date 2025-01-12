class Solution:
    def isValid(self, s: str) -> bool:
        # Dictionary to match every closing brackets to its opening
        matching_brackets = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        # Stack to store the opening brackets
        stack = []
        
        for c in s:
            # If the character is an opening brackets
            if c in matching_brackets.values():  # Opening brackets
                stack.append(c)
            elif c in matching_brackets:  # Closing brackets (keys)
                # If we find a closing bracket but the stack is empty, that means there isn't a corresponding
                # opening bracket: a closing bracket appears before its opening one
                # Also, if the closing bracket doesn't match the last opening bracket
                if not stack or stack.pop() != matching_brackets[c]:
                    return False
        
        # Check if the stack is empty to ensure all opening brackets were closed and no opening brackets left
        return not stack