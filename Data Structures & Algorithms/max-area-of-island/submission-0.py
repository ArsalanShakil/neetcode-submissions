class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        maxArea = 0

        def dfs(rows,cols):
            if (rows < 0 or rows >= len(grid) or cols < 0 or cols >= len(grid[0]) or grid[rows][cols] != 1):
                return 0
            else:
                grid[rows][cols] = 0
                return 1 + dfs(rows+1, cols) + dfs(rows-1,cols) + dfs(rows, cols+1) + dfs(rows, cols-1)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r,c))

        return maxArea
