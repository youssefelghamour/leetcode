class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Both implementations work
        """
        s_dict = {}
        t_dict = {}
        
        for char in s:
            if char not in s_dict:
                s_dict[char] = 1
            else:
                s_dict[char] += 1
        
        for char in t:
            if char not in t_dict:
                t_dict[char] = 1
            else:
                t_dict[char] += 1
        
        return t_dict == s_dict
        """
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)