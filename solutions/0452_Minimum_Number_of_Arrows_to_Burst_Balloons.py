from utils import timer

class Solution:
    
    # Solution 1: Greedy
    @timer
    def findMinArrowShots(self, points):
        if len(points) == 1:
            return 1

        points = sorted(points, key=lambda x: x[0])
        right = points[0][1]
        arrows = 1
        for i in range(1, len(points)):
            if right >= points[i][0]:
                right = min([right, points[i][1]])
            else:
                arrows += 1
                right = points[i][1]

        return arrows




if __name__ == "__main__":
    sol = Solution()
    print(sol.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))
    print(sol.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))
    print(sol.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]))