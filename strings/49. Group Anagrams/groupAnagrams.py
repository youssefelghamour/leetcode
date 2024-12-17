class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        result = []
        skip_list = [] # Contains indices of the element that have already been added to a sublist
        count = 0
        
        for i in range(len(strs)):
            # Skip the current element if it has already been added to a sublist
            if i not in skip_list:
                # Create a sublist for the anagram with the current element
                result.append([strs[i]])

                # Iterate over the rest of the elements
                for j in range(i + 1, len(strs)):
                    # If the element are ... and the current element hasn't been added yet
                    if sorted(strs[i]) == sorted(strs[j]) and j not in skip_list:
                        # Add the element to the sublist
                        result[count].append(strs[j])
                        # Add the j index to skip_list so it's skiped during next iterations
                        skip_list.append(j)

                # Points to the index of the sublist in result
                count += 1
        
        return result
        """
        d = {}
    
        for s in strs:
            k = "".join(sorted(s))  # Sort the string to create a key

            if k not in d:
                d[k] = []  # Initialize the list if the key doesn't exist

            d[k].append(s)  # Add the string to the corresponding key

        return list(d.values())