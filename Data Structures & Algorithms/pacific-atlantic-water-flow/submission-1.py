class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit # if visited before
            # out of bounds
            or r < 0 or c < 0 or r == ROWS or c == COLS
            # if height is NOT greater than or equal to curr height
            or heights[r][c] < prevHeight):
                return
            
            # add to set
            visit.add((r, c))

            # iterate on all 4 adjacent tiles
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(COLS):
            # first row and go column by column
            dfs(0, c, pac, heights[0][c])
            # bottom row and go column by column
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            # first column and go row by row
            dfs(r, 0, pac, heights[r][0])
            # last column and go row by row
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []
        # for every single cell, check if it overlaps between the sets
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res





