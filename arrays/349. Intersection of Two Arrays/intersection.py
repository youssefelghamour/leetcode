class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))

        for n in nums1:
            if n in nums2:
                result.append(n)
        
        return result
        """
        # To make it faster we can use sets
        set1 = set(nums1)
        set2 = set(nums2)

        # Return the intersection of both sets
        return list(set1 & set2)
        """