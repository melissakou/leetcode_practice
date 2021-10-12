class Solution:
    # Brute Force O(n^2)
    # def twoSum(self, nums, target):
    #     for i in range(len(nums)):
    #         for j in range(i+1, len(nums)):
    #             if nums[i] + nums[j] == target:
    #                 return [i, j]

    # Hash table to store the seen numbers
    def twoSum(self, nums, target):
        seen_value = {}
        for i, num in enumerate(nums):
            remain = target - num
            if remain in seen_value:
                return [i, seen_value[remain]]
            else:
                seen_value[num] = i

    # Two Pointers
    # def twoSum(self, nums, target):
    #     nums_sorted = [(value, i) for i, value in enumerate(nums)]
    #     nums_sorted.sort()

    #     left, right = 0, len(nums) - 1
    #     while left < right:
    #         curr_sum = nums_sorted[left][0] + nums_sorted[right][0]
    #         if curr_sum == target:
    #             return [nums_sorted[left][1], nums_sorted[right][1]]
    #         elif curr_sum < target:
    #             left += 1
    #         else:
    #             right -= 1



if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2,7,11,15], 9))
    print(sol.twoSum([3,2,4], 6))
    print(sol.twoSum([3,3], 6))