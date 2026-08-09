class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort intervals by start value
        intervals.sort(key = lambda i : i[0])
        res = [intervals[0]]

        # looping through start and end value, skipping the first one
        for start, end in intervals[1:]:
            # get most recent value 
            lastEnd = res[-1][1]

            if start <= lastEnd:
                res[-1][1] = max(lastEnd, end)
            else:
                res.append([start, end])

        return res