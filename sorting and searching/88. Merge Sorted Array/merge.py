class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1  # The end of nums1
        p2 = n - 1  # The end of nums2
        p = m + n - 1  # The end of the merged array
        
        # Start from the end and put the larger elements at the end in nums1
        while p1 >= 0 or p2 >= 0:
            if p1 < 0:  # If nums1 is exhausted, copy the rest of nums2
                nums1[p] = nums2[p2]
                p2 -= 1
            elif p2 < 0:  # If nums2 is exhausted, copy the rest of nums1
                nums1[p] = nums1[p1]
                p1 -= 1
            else:  # Compare and put the larger element at the end
                if nums1[p1] > nums2[p2]:
                    nums1[p] = nums1[p1]
                    p1 -= 1
                else:
                    nums1[p] = nums2[p2]
                    p2 -= 1
            p -= 1