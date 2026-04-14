from collections import deque

class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        senate = list(senate)
        d_queue = deque()
        r_queue = deque()

        # Add indexes of each type of senate to their queue
        for i, senator in enumerate(senate):
            if senator == "R":
                r_queue.append(i)
            else:
                d_queue.append(i)
        
        # Compare the indexes: the lowest (comes first) eliminates the other
        # In case one wins we add it to the ende of the queue so they can pariticpate in the next round
        while d_queue and r_queue:
            d = d_queue.popleft()
            r = r_queue.popleft()

            if r < d:
                r_queue.append(r + len(senate))
            else:
                d_queue.append(d + len(senate))
        
        return "Radiant" if r_queue else "Dire"