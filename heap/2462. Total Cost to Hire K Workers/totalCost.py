import heapq
class Solution(object):
    def totalCost(self, costs, k, candidates):
        """
        :type costs: List[int]
        :type k: int
        :type candidates: int
        :rtype: int
        """
        cost = 0
        left_heap = []
        right_heap = []
        # Pointers marking the next elements to add to heap
        l = 0  # next unused from the left side
        r = len(costs) - 1  # next unused from the right side

        while l < candidates and l <= r:
            heapq.heappush(left_heap, costs[l])
            l += 1

        while r >= len(costs) - candidates and l <= r:
            heapq.heappush(right_heap, costs[r])
            r -= 1

        while k > 0:
            if not right_heap or (left_heap and left_heap[0] <= right_heap[0]):
                cost += heapq.heappop(left_heap)
                if l <= r:
                    heapq.heappush(left_heap, costs[l])
                    l += 1
            else:
                cost += heapq.heappop(right_heap)
                if l <= r:
                    heapq.heappush(right_heap, costs[r])
                    r -= 1

            k -= 1
        
        return cost