class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Hash map holding characters from s as keys mapped to character from t as values (s: t)
        char_map = {}

        for i in range(len(s)):
            if s[i] not in char_map:  # Check if s[i] doesn't exist as a key
                if t[i] in char_map.values():  # t[i] shouldn't exist since they should be mapped together
                    return False  # If it does, it means t[i] is mapped to a different char from s
                    """ s = "badc"
                        t = "baba"
                        -> i = 2: s[i] = d, doesn't exist as key, but t[i] = b exists as value and is mapped to b,
                            return False
                    """
                char_map[s[i]] = t[i]  # Both don't exist, create a new pair
            else:
                # Since s[i] exists as key it should be mapped to t[i] as value
                if t[i] != char_map[s[i]]:
                    return False
        
        return True