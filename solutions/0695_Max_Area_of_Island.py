from utils import timer
from itertools import product

class Solution:
    
    # Solution 1: DFS
    @timer
    def maxAreaOfIsland(self, grid):
        rows, cols = len(grid), len(grid[0])
        area = 0

        def calculate_area(i, j):
            if (i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 0):
                return 0
            grid[i][j] = 0 # mark as visited
            return 1 + calculate_area(i+1, j) \
                     + calculate_area(i-1, j) \
                     + calculate_area(i, j+1) \
                     + calculate_area(i, j-1)
        
        for i, j in product(range(rows), range(cols)):
            if grid[i][j]:
                area = max(area, calculate_area(i, j))

        return area


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))
    print(sol.maxAreaOfIsland([[0,0,0,0,0,0,0,0]]))