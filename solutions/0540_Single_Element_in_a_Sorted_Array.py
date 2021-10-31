from utils import timer

class Solution:

    # Solution 1: Binary Search
    @timer
    def singleNonDuplicate(self, nums):
        if len(nums) == 1: return nums[0]
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid-1] != nums[mid] and nums[mid] != nums[mid+1]: return nums[mid]
            if mid % 2 == 0:
                if nums[mid] == nums[mid+1]: left = mid + 1
                else: right = mid - 1
            else:
                if nums[mid] == nums[mid+1]: right = mid - 1
                else: left = mid + 1

        return nums[left]


if __name__ == "__main__":
    sol = Solution()
    print(sol.singleNonDuplicate([1,1,2,3,3,4,4,8,8]))
    print(sol.singleNonDuplicate([3,3,7,7,10,11,11]))
