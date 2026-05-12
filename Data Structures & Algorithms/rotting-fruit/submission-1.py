class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        nums_fresh = 0 
        time = 0
        ROWS, COLS = len(grid), len(grid[0])
        EMPTY, FRESH, ROTTEN,  = 0, 1, 2
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == FRESH:
                    nums_fresh += 1
                elif grid[r][c] == ROTTEN:
                    q.append([r,c])
        
        while q and nums_fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for row_change, col_change in directions:
                    row, col = r + row_change, c + col_change
                    if (row < 0 or row == len(grid) 
                        or col < 0 or col == len(grid[0]) 
                        or grid[row][col]!=1):
                        continue 
                    grid[row][col] = 2
                    q.append([row,col])
                    nums_fresh -=1
            time +=1
        return time if nums_fresh == 0 else -1

