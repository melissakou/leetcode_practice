from time import time
from utils import timer

class Solution:

    # Solution 1: Binary Search
    # @timer
    # def mySqrt(self, x):
    #     if x == 1: return 1
    #     left, right = 0, x
    #     mid = (left + right) // 2
    #     while left != mid and right != mid:
    #         if mid ** 2 == x: return mid
    #         if left ** 2 <= x and x < mid ** 2: right = mid
    #         elif mid ** 2 < x and x <= right ** 2: left = mid
    #         mid = (left + right) // 2
    #     return left

    # Solution 2: Newton's method
    @timer
    def mySqrt(self, x):
        x_n = x
        while x_n ** 2 > x:
            x_n = int((x_n + x / x_n) / 2)
        return x_n


if __name__ == "__main__":
    sol = Solution()
    print(sol.mySqrt(4))
    print(sol.mySqrt(8))