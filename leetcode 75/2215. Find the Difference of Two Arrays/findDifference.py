class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        answer = [[], []]
        # Lookup in a set is O(1) vs O(n) in an array
        # Also removes duplicates
        set1 = set(nums1)
        set2 = set(nums2)
        
        for n in set1:
            if n not in set2:
                answer[0].append(n)
        
        for m in set2:
            if m not in set1:
                answer[1].append(m)
        
        return answer