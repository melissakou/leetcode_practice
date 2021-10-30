from utils import timer

class Solution:

    # Binary Serach + Recursive
    @timer
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target: return True
             
            if nums[mid] == nums[left]: left += 1
            elif nums[mid] == nums[right]: right -= 1
            elif nums[mid] > nums[left]:
                if target < nums[left]: left = mid + 1
                else:
                    if target > nums[mid]: left = mid + 1
                    else: right = mid - 1
            else:
                if target >= nums[left]: right = mid - 1
                else:
                    if target > nums[mid]: left = mid + 1
                    else: right = mid - 1
        return False



if __name__ == "__main__":
    sol = Solution()
    print(sol.search(nums=[2,5,6,0,0,1,2], target=0))
    print(sol.search(nums=[2,5,6,0,0,1,2], target=3))