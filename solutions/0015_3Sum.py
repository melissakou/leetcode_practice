from operator import le

from numpy import sort


class Solution:

    # Solution 1. Naive Solution, Brute Force
    # Time Complexity: O(n^3)
    # Space Complexity: O(1)
    def threeSum(self, nums):
        ans = set()
        def twoSum(nums, target):
            for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    if nums[i] + nums[j] == target:
                        ans.add(tuple(sorted([0 - target, nums[i], nums[j]])))

        for i in range(len(nums)):
            twoSum(nums[i+1:], 0 - nums[i])

        return ans

    # Solution 2. Two Pointers
    # Time Complexity: O(nlogn) + O(n^2)
    # Space Complexity: O(1)
    def threeSum(self, nums):
        nums = sorted(nums)
        ans = set()

        def twoSum_withSorted(nums, target):
            l, r = 0, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    ans.add((0 - target, nums[l], nums[r]))
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1

        for i in range(len(nums)-2):
            if nums[i] + nums[i+1] + nums[i+2] > 0:
                break
            if nums[i] + nums[-1] + nums[-2] < 0:
                continue
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            twoSum_withSorted(nums[i+1:], 0 - nums[i])

        return ans

    # Solution 3. Hash Map
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    def threeSum(self, nums):
        ans = set()

        def twoSum(nums, target):
            seen = set()
            for i in range(len(nums)):
                if target - nums[i] in seen:
                    ans.add(tuple(sorted([0 - target, target - nums[i], nums[i]])))
                seen.add(nums[i])

        for i in range(len(nums)):
            twoSum(nums[i+1:], 0 - nums[i])

        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSum([-1,0,1,2,-1,-4]))
    print(sol.threeSum([0,1,1]))
    print(sol.threeSum([0,0,0]))