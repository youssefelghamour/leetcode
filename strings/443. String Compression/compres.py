class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i = 0
        j = 0

        while i < len(chars):
            # If there is a group of consecutive repeating characters
            if i + 1 < len(chars) and chars[i + 1] == chars[i]:
                # Index to help count the length of the group
                j = i

                while j < len(chars) and chars[j] == chars[i]:
                    j += 1
                # Counts how many characters in the group
                count = j - i

                # Make the replacement: 'char', 'count'
                # count is turned into a string so if it's more than 10, ex 112, it becomes '1', '1', '2'
                # replacement in that case would be: 'char', '1', '1', '2'
                replacement = [chars[i]] + list(str(count))

                # Replace the group of characters
                chars[i:j] = replacement

                # Advance th read index by the length if the replacement to get to the new characters in chars
                i += len(replacement)
            else:
                # Only one single non-repeating character
                i += 1
        
        return len(chars)