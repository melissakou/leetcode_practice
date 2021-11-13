from utils import timer

class Solution:

    # Solution 1: Build-in sort
    # @timer
    # def sortColors(self, nums):
        
    #     nums.sort()

    # Solution 2: Two Pointers (Dutch national flag problem)
    @timer
    def sortColors(self, nums):
        i, j, k = 0, 0, len(nums) - 1

        while j <= k:
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1 ; j += 1
            elif nums[j] == 1: j += 1
            else:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1


if __name__ == "__main__":
    sol = Solution()
    sol.sortColors([2,0,2,1,1,0])
    sol.sortColors([2,0,1])
    sol.sortColors([0])
    sol.sortColors([1])