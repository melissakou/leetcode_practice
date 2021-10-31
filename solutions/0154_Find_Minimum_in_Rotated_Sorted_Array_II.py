from utils import timer

class Solution:
    
    # Solution 1: Binary Search
    @timer
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        while left + 1 <= right and nums[left] == nums[left+1]: left += 1
        while right - 1 >= left and nums[right] == nums[right-1]: right -= 1
        while left < right:
            while left + 1 <= right and nums[left] == nums[left+1]: left += 1
            while right - 1 >= left and nums[right] == nums[right-1]: right -= 1
            mid = (left + right) // 2
            if nums[mid-1] > nums[mid] and nums[mid+1] > nums[mid]: return nums[mid]
            elif nums[mid] >= nums[left] and nums[mid] >= nums[right]: left = mid + 1
            else: right = mid

        return nums[left]


if __name__ == "__main__":
    sol = Solution()
    print(sol.findMin([1,3,5]))
    print(sol.findMin([2,2,2,0,1]))
    