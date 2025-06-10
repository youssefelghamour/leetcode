class Solution(object):
    def clearStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        result = []

        for i in range(len(s)):
            if s[i] == '*':
                lex_smallest = result[0]  # initialize the min from result, not s
                k = 0  # index of the lex smallest char

                for j in range(len(result)):
                    # find the lex smallest rightmost char
                    if result[j] <= lex_smallest:
                        lex_smallest = result[j]
                        k = j
                
                result.pop(k)
            else:
                result.append(s[i])
        
        return ''.join(result)
        """
        s = list(s)
        result = []
        positions = {}  # stores the characters from result as indexes, and a list of ther position in result as values

        for i in range(len(s)):
            if s[i] == '*':
                # look for the smallest lex char in result (first find)
                for char in "abcdefghijklmnopqrstuvwxyz":
                    # the first char we find a non empty value in the dict is the smallest lex in result
                    # we take the last value from positions[char] = [i , j , idx] that'd be the rightmost
                    if char in positions and positions[char]:
                        idx = positions[char].pop()
                        # mark the lex smallest char in s to be removed
                        s[idx] = '*'
                        break
            else:
                # add this char to the dict
                if s[i] in positions:
                    positions[s[i]].append(i)
                else:
                    positions[s[i]] = [i]
        
        for c in s:
            if c != '*':
                result.append(c)

        return ''.join(result)