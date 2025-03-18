class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []

        for n in nums1:
            found = False

            for i in range(len(nums2)):
                if n == nums2[i]:
                    # Look for the next greater element amongst all the rest element to the right
                    for j in range(i + 1, len(nums2)):
                        if nums2[j] > n:
                            ans.append(nums2[j])
                            found = True
                            break

            # No next greater element found
            if not found:
                ans.append(-1)
        
        return ans