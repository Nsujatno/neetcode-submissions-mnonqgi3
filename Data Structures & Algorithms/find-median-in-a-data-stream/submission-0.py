class MedianFinder:

    def __init__(self):
        # two heaps, large and small
        # small is max heap, large is min heap
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # in python theres no max heap so we multiply by -1
        heapq.heappush(self.small, -1 * num)

        # make sure every element in small is less than every num in large
        if (self.small and self.large and (-1 * self.small[0]) > self.large[0]):
            # if not then pop it and push to large
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # uneven size?
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0] * -1
        if len(self.large) > len(self.small):
            return self.large[0]
        
        # even num of elements
        return (self.small[0] * -1 + self.large[0]) / 2
