class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # ends before it starts
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                # since the rest are fine, we just return the rest of the intervals
                return res + intervals[i:]
            # new interval goes after the interval we are at
            elif newInterval[0] > intervals[i][1]:
                # append interval we are at bc its not overlapping
                # DONT append newinterval bc it could technically overlap the next interval
                res.append(intervals[i])
            # the new interval overlaps
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
                # dont add bc it could overlap the next interval
        
        res.append(newInterval)
        return res
