from utils import timer
from itertools import product

class Solution:

    # Solution 1: DFS
    @timer
    def pacificAtlantic(self, heights):
        m, n = len(heights), len(heights[0])
        can_flow_pacific = set()
        can_flow_atlantic = set()

        def flow_back(i, j, visited_set, prev_height):
            if (i, j) in visited_set or \
                i < 0 or j < 0 or i >= m or j >= n or \
                heights[i][j] < prev_height:
                return

            visited_set.add((i,j))
            flow_back(i-1, j, visited_set, heights[i][j])
            flow_back(i+1, j, visited_set, heights[i][j])
            flow_back(i, j-1, visited_set, heights[i][j])
            flow_back(i, j+1, visited_set, heights[i][j])
            

        for i in range(m):
            flow_back(i, 0, can_flow_pacific, -float("infinity"))
            flow_back(i, n-1, can_flow_atlantic, -float("infinity"))
        
        for j in range(n):
            flow_back(0, j, can_flow_pacific, -float("infinity"))
            flow_back(m-1, j, can_flow_atlantic, -float("infinity"))
        
        return list(can_flow_pacific.intersection(can_flow_atlantic))


if __name__ == "__main__":
    sol = Solution()
    print(sol.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
    print(sol.pacificAtlantic([[2,1],[1,2]]))