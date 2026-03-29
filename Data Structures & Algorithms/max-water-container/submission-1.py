class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        so basically
        two pointers l and r, at 0 and the end.
        height of container is the smallest val between l and r
        width of container is r - l
        store max

        when to move l and r pointers?
        we move the shorter height pointer
        """
        area = 0
        l, r = 0, len(heights) - 1
        while l < r:
            height = min(heights[l], heights[r])
            width = r - l
            area = max(area, height * width)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return area
