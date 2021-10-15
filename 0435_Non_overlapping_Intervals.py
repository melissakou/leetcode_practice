from utils import timer

class Solution:

    # Solution 1. Greedy
    @timer
    def eraseOverlapIntervals(self, intervals):
        if len(intervals) == 1:
            return 0
        
        intervals = sorted(intervals, key=lambda x: x[1])
        right = intervals[0][1]
        remove = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < right:
                remove += 1
            else:
                right = intervals[i][1]

        return remove


if __name__ == "__main__":
    sol = Solution()
    print(sol.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
    print(sol.eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
    print(sol.eraseOverlapIntervals([[1,2],[2,3]]))