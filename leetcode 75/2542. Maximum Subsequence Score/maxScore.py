import heapq
class Solution(object):
    def maxScore(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        #
        n1_sum = 0
        result = 0
        min_heap = []
        pairs = []

        for i in range(len(nums2)):
            pairs.append((nums2[i], nums1[i]))

        pairs.sort(reverse=True)

        for n2, n1 in pairs:
            n1_sum += n1
            heapq.heappush(min_heap, n1)

            if len(min_heap) > k:
                popped_n1 = heapq.heappop(min_heap)
                n1_sum -= popped_n1
            if len(min_heap) == k:
                result = max(result, n1_sum * n2)
        
        return result