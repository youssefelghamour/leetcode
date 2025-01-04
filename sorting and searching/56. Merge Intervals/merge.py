class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:        
        i = 0
        
        while i < len(intervals):
            j = i + 1
            # Go through all intervals after i and check against the i interval
            while j < len(intervals):
                # Check if intervals overlap
                # For intervals[i] = [a,b], intervals[j] = [c,d]: If c <= b and d >= a
                if intervals[j][0] <= intervals[i][1] and intervals[j][1] >= intervals[i][0]:
                    start = min(intervals[i][0], intervals[j][0])
                    end = max(intervals[i][1], intervals[j][1])
                    # Update the i th interval with the merged one
                    intervals[i] = [start, end]
                    # Delete the j th interval since it was merged
                    del intervals[j]
                    # Reset j to i+1 to recheck the newly merged interval against the remaining ones
                    j = i + 1
                # If no overlap
                else:
                    # Move to the next interval
                    j += 1
            # Move to the next interval after checking all overlaps for current i
            i += 1
        
        return intervals