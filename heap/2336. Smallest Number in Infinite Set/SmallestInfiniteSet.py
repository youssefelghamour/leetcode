"""
We use:
    - a min heap that holds numbers that were removed from the set and added back (so the smallest re-added number is always on top)
    - a next variable initialized at 1 that always points to the next number to remove from the set

When we pop:
    - if the heap is not empty -> pop from the heap first
    - otherwise -> return next and increment it
    - this works because the heap only contains numbers that were already removed before, so they are always < next

When we addBack:
    - we only add a number to the heap (and set) if it is < next
    - otherwise we ignore it (because it was never removed from the set in the first place)
"""
import heapq

class SmallestInfiniteSet(object):

    def __init__(self):
        self.next = 1
        self.heap = []

    def popSmallest(self):
        """
        :rtype: int
        """
        if self.heap:
            return heapq.heappop(self.heap)
        else:
            tmp = self.next
            self.next += 1
            return tmp

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num < self.next and num not in self.heap:
            heapq.heappush(self.heap, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)