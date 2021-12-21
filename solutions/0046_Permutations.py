from time import time
from utils import timer

class Solution:

    # Solution 1: Backtracking
    @timer
    def permute(self, nums):
        if len(nums) <= 1:
            return [nums]
        
        answer = []
        for i, n in enumerate(nums):
            other_nums = nums[:i] + nums[i+1:]
            for p in self.permute(other_nums):
                answer.append([n] + p)
            
        return answer


if __name__ == "__main__":
    sol = Solution()
    print(sol.permute([1,2,3]))
    print(sol.permute([0,1]))