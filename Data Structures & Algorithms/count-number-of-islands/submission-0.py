class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        BFS?
        go through each index and if its 1, do bfs on it
        need to keep track of islands we've visited before
        """
        def bfs(row, column):
            queue = []
            directions = [(0,1), (0,-1), (1,0), (-1,0)]
            # add to queue and visited
            queue.append((row, column))
            visited.add((row, column))
            
            while len(queue) > 0:
                curr = queue.pop(0)
                for dr, dc in directions:
                    new_row = curr[0] + dr
                    new_column = curr[1] + dc
                    # print(new_row, new_column)

                    if 0 <= new_row < len(grid) and 0 <= new_column < len(grid[0]):
                        if grid[new_row][new_column] == "1" and (new_row, new_column) not in visited:
                            print(new_row, new_column)
                            queue.append((new_row, new_column))
                            visited.add((new_row, new_column))
            print("done w bfs")

        # initialize visited and island count
        visited = set()
        num_of_islands = 0
        # iterate through every elements
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                # if its 1, increment island count, call bfs
                # print(grid[i][j])
                if grid[i][j] == "1" and (i, j) not in visited:
                    num_of_islands += 1
                    bfs(int(i), int(j))


        return num_of_islands
