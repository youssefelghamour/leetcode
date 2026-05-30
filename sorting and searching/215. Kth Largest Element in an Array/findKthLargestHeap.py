import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        1. First approach:
            - Insert all elements into a max heap
            - Go through the head with a loop until we reach k
            -> requires O(n) to insert into heap + k * each pop O(log(n)) = O(n + k log(n) )
        2. Second approach:
            - Insert elements into a min heap
            - when we reach size k, we pop the smallest element of the heap
              benefiting from the property of min heap.
            - our heap will be similar to a sliding window keeping only the k max values
            - kth largest is the first pop
            -> Faster
        """
        min_heap = []

        for n in nums:
            heapq.heappush(min_heap, n)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return heapq.heappop(min_heap)