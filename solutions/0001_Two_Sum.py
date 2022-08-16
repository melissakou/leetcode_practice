class Solution:

    # Solution 1. Naive Solution, Brute Force
    # Time Complexity: O(n^2)
    # Space Complexity: O(1) 
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

    # Solution 2. Sorting + Two Pointers
    # Time Complexity: O(nlogn) + O(n)
    # Space Complexity: O(n)
    def twoSum(self, nums, target):
        sorted_idx = sorted(range(len(nums)), key=lambda k: nums[k])
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[sorted_idx[l]] + nums[sorted_idx[r]] == target:
                return [sorted_idx[l], sorted_idx[r]]
            elif nums[sorted_idx[l]] + nums[sorted_idx[r]] > target:
                r -= 1
            else:
                l += 1

    # Solution 3. Hash Map
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def twoSum(self, nums, target):
        seen = {}
        for i in range(len(nums)):
            if target - nums[i] in seen:
                return [seen[target - nums[i]], i]
            seen[nums[i]] = i





if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2,7,11,15], 9))
    print(sol.twoSum([3,2,4], 6))
    print(sol.twoSum([3,3], 6))