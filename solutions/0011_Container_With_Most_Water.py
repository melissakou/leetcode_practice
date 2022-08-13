from re import I
from requests import head


class Solution:

    # Solution 1: Naive Solution
    def maxArea(self, height):
        max_area = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                w = j - i
                h = min(height[i], height[j])
                area = w * h
                max_area = max(max_area, area)

        return max_area

    # Solution 2: Two Pointers
    def maxArea(self, height):
        l, r = 0, len(height) - 1
        max_area = 0
        while l <= r:
            area = (r - l) * min(height[r], height[l])
            max_area = max(max_area, area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1

        return max_area


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxArea([1,8,6,2,5,4,8,3,7])) #49
    print(sol.maxArea([1,1])) #1
    print(sol.maxArea([1,2,1])) #2
    print(sol.maxArea([1,2,4,3])) #4
    print(sol.maxArea([2,3,4,5,18,17,6])) #17