from utils import timer

class Solution:

    # Solution 1: Greedy
    @timer
    def checkPossibility(self, nums):
        nums = [-1e5, -1e5] + nums
        modify = False
        for i in range(2, len(nums)):
            if nums[i-1] <= nums[i]:
                continue
            if not modify:
                if nums[i] >= nums[i-2]: nums[i-1] = nums[i-2]
                else: nums[i] = nums[i-1]
                modify = True
            else:
                return False
  
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.checkPossibility([4,2,3])) #True
    print(sol.checkPossibility([4,2,1])) #False