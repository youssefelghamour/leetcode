class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]

        ex: s = "ababcbacadefegdehijhklij", char_occ = { 'a': 8, 'b': 5, ... }
            - Iteration 1: end = 0 < char_occ['a'] = 8, end = 8
            - Iteration 2: end = 8 > char_occ['b'] = 5, so end stays 8
            ...
            - Iteration 4: end = 8 > char_occ['c'] = 7, so end stays 8
            ...
            - Iteration 9: i = 8 == end, partition the substring s[start:end+1] including the last element,
                            result.append(len(s[start:end + 1])) or result.append(end + 1 - start)
                
            *** Second approach:
            - Iteration 1: i = 0 < char_occ['a'] = 8, end = 8
            - Iteration 2: i = 1 < char_occ['b'] = 5, but end = 8 > char_occ['b'], so end stays 8
            ...
            - Iteration 4: i = 5 < char_occ['c'] = 7, but end = 8 > char_occ['c'], so end stays 8
            ...
        """
        result = []
        # Hash table that holds index of the last occurence of every char in s
        char_occ = {}
        start = 0  # Start of the substring
        end = 0  # End of the substring

        for i in range(len(s)):
            char_occ[s[i]] = i
        
        for i in range(len(s)):
            """
            # second approach
            # If there's another occurence of this character ahead, we can't partition yet
            if i < char_occ[s[i]] and end < char_occ[s[i]]:
                end = char_occ[s[i]]
            """
            # Keep track of the max of previous end and the last occurence of this char
            end = max(end, char_occ[s[i]])

            if i == end:
                result.append(end + 1 - start)
                start = end + 1
                # end += 1, second approach requires end to be incremented
                # because i < char_occ[s[i]] might prevent end from updating
                # (ex: "eaaaabaaec", when i=9 not < char_occ['c'] = 9 & end stays 8 and i != end, we never add c)
        
        return result