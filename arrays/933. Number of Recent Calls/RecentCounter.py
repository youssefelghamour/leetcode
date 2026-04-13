from collections import deque

class RecentCounter(object):

    def __init__(self):
        self.requests = deque()
        # self.requests = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.requests.append(t)
        
        """
        i = 0
        while i < len(self.requests) and self.requests[i] < t - 3000:
            i += 1
        self.requests = self.requests[i:]
        """

        while self.requests[0] < t - 3000:
            self.requests.popleft()
            
        return len(self.requests)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)