class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        res = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            # not overlapping
            if start >= prevEnd:
                prevEnd = end
            # they are overlapping
            else:
                # "remove" one of the intervals
                res += 1
                # keep minimum end value
                prevEnd = min(prevEnd, end)

        return res