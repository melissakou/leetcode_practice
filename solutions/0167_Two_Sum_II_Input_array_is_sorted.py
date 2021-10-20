from utils import timer

class Solution:

    # Solution 1: save seen number to hashtable
    # @timer
    # def twoSum(self, numbers, target):
    #     seen = {}
    #     for i, n in enumerate(numbers):
    #         remain = target - n
    #         if seen.get(remain) is not None:
    #             return [seen[remain]+1, i+1]
    #         else:
    #             seen[n] = i

    # Solution 2: Two Pointers
    @timer
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers)-1
        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                return [left+1, right+1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum(numbers=[2,7,11,15], target=9))
    print(sol.twoSum(numbers=[2,3,4], target=6))
    print(sol.twoSum(numbers=[-1,0], target=-1))
