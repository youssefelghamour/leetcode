class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        occ = {}  # key: arr[i], val: occurrence

        for n in arr:
            occ[n] = occ.get(n, 0) + 1
        
        # Turn the values into a set to remove duplicates
        occ_set = set(list(occ.values()))

        # If duplicates exist then the length will be different (smaller)
        # Check if duplicate occurences exist, return false
        """
        if len(list(occ.values())) != len(occ_set):
            return False
        else:
            return True
        """
        return len(occ.values()) == len(set(occ.values()))