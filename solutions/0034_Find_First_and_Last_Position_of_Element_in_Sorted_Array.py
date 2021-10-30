from utils import timer

class Solution:

    # Solution 1: Binary Search
    @timer
    def searchRange(self, nums, target):
        def binary_search(nums, target, lower):
            left, right = 0, len(nums) - 1
            index = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target: right = mid - 1
                elif nums[mid] < target: left = mid + 1
                else:
                    index = mid
                    if lower: right = mid - 1
                    else: left = mid + 1
            return index
        
        lower = binary_search(nums, target, True)
        upper = binary_search(nums, target, False)

        return [lower, upper]


if __name__ == "__main__":
    sol = Solution()
    print(sol.searchRange(nums=[5,7,7,8,8,10], target=8))
    print(sol.searchRange(nums=[5,7,7,8,8,10], target=6))
    print(sol.searchRange(nums=[], target=0))