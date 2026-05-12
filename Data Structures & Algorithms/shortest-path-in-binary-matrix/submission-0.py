
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        grid_size = len(grid)
        places_to_visit = deque([(0,0,1)])
        places_visited = set()
        places_visited.add((0,0))
        directions = [[-1, -1], [-1, 0], [-1, 1],[ 0, -1],
                        [ 0, 1],[ 1, -1], [ 1, 0], [ 1, 1]]

        while places_to_visit:
            row, col, path_length = places_to_visit.popleft()
            if (min(row,col) < 0 or max(row,col) >= grid_size or grid[row][col]):
                continue 
            if row == grid_size-1 and col == grid_size-1:
                return path_length
            for row_change, col_change in directions:
                neighbour = (row+row_change, col+col_change)
                if neighbour not in places_visited:
                    places_to_visit.append((neighbour[0],neighbour[1], path_length + 1))
                    places_visited.add(neighbour)
        return -1
            
