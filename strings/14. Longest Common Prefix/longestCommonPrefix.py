class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        
        # Find the element with the smallest length
        # shortest_string = min(strs, key=len)
        shortest_string = strs[0]
        for s in strs:
            if len(s) < len(shortest_string):
                shortest_string = s
        
        # Iterate through the samelled string, and check each character
        for i in range(len(shortest_string)):
            # If all strings include the character, add it to the prefix
            if all(current_string[i] == shortest_string[i] for current_string in strs):
                prefix += shortest_string[i]
            else:
                break
        
        return prefix