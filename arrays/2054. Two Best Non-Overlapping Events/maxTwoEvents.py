class Solution(object):
    def maxTwoEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int

        Process:

        1. We sort the list of events by start time in ascending order

        2. We make a best_from_here list by going backwards through our sorted events list:
            - At each event i we keep track of the maximum value from i onward
            - Example: values = [3, 1, 5, 2]:
                a. Start backwards: last value is 2 -> best_from_here[3] = 2
                b. Move to index 2: max(5, 2) = 5 -> best_from_here[2] = 5
                c. Index 1: max(1, 5) = 5 -> best_from_here[1] = 5
                d. Index 0: max(3, 5) = 5 -> best_from_here[0] = 5 
        
        3. We iterate though events, for each current event we look for an event that starts after it (start_j > end_i)
            - We use binary search to find the optimal start date: event with earlier start date after our event ends:
                - Check the middle start time
                - If it’s ≤ current end -> move right
                - If it’s > current end -> move left (it could be the answer)
            - The one we land on is the exact next non overlapping event j
            - From here all events after j can potentially be a next event of i too
            - So we just need to find the max of the events from j onward in best_from_here[j]
            - Add current event i value to best_from_here[j] and we have the max values we can get if we choose to start with event i
        """
        n = len(events)
        max_sum = 0
        best_from_here = [0] * n

        # Sort the list by events start time
        events.sort(key=lambda event: event[0])
        
        # Fill best_from_here
        # The last event has no following events so the best value starting from it is its own value
        best_from_here[n - 1] = events[n - 1][2]
        for i in range(n - 2, -1, -1):
            current_event_value = events[i][2]
            best_from_here[i] = max(current_event_value, best_from_here[i + 1])
        
        print(best_from_here)
        
        for i in range(n):
            current_event = events[i]
            current_event_value = events[i][2]
            # Binary search to find the just next event
            left = i + 1
            right = n - 1
            while left <= right:
                mid = (left + right) // 2
                # If events[mid].start > events[i].end
                if events[mid][0] > events[i][1]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            # If there is no next event left will be n
            if left < n:
                # best_from_here[left]: max from all potential next events
                current_max_sum = current_event_value + best_from_here[left]
            else:
                current_max_sum = current_event_value  # no next event
            
            max_sum = max(max_sum, current_max_sum)
        
        return max_sum