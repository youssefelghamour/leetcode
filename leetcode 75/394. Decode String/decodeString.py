class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        i = 0

        while i < len(s):
            if s[i] != "]":
                # Add all characters to the stack including [ until ] is found
                stack.append(s[i])
            else:
                substring = ""

                # Get the substring between brackets from the stack
                while stack and stack[-1] != "[":
                    # So tmp is not reversed
                    substring = stack.pop() + substring

                # remove "["
                stack.pop()

                num = ""
                # Get the whole number
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num

                stack.append(substring * int(num))
            i += 1
        
        return "".join(stack)