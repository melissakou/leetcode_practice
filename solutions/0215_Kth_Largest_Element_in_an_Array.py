from utils import timer

class Solution:

    # Solution 1: Build-in sort
    # @timer
    # def findKthLargest(self, nums, k):
    #     nums = sorted(nums, key=lambda x: -x)
    #     return nums[k-1]

    # Solution 2: Quick Selection
    # @timer
    # def findKthLargest(self, nums, k):
    #     def quick_selection(nums, left, right):
    #         if right - left >= 1:
    #             i, j = left, right
    #             pivot = nums[left]
    #             while i != j:
    #                 while nums[j] >= pivot and i < j: j -= 1
    #                 while nums[i] <= pivot and i < j: i += 1
    #                 if i < j: nums[i], nums[j] = nums[j], nums[i]
    #             nums[left], nums[i] = nums[i], nums[left]

    #             return i
    #         else: return left

    #     l, r = 0, len(nums) - 1
    #     while l <= r:
    #         pivot = quick_selection(nums, l, r)
    #         largest_k = len(nums) - pivot
    #         if largest_k == k: return nums[pivot]
    #         elif largest_k < k: r = pivot - 1
    #         else: l = pivot + 1

    # Solution 3: Heap Sort
    @timer
    def findKthLargest(self, nums, k):
        def swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]
        
        def heapify(nums, i, upper):
            l, r = i*2+1, i*2+2
            if r <= upper and nums[l] > nums[i] and nums[r] > nums[i]:
                if nums[l] >= nums[r]:
                    swap(nums, i, l) ; heapify(nums, l, upper)
                else:
                    swap(nums, i, r) ; heapify(nums, r, upper)
            elif l <= upper and nums[l] > nums[i]:
                swap(nums, i, l) ; heapify(nums, l, upper)
            elif r <= upper and nums[r] > nums[i]:
                swap(nums, i, r) ; heapify(nums, r, upper)

        for i in range((len(nums)-2)//2, -1, -1):
            heapify(nums, i, len(nums)-1)
            
        end = len(nums) - 1
        for _ in range(k):
            swap(nums, 0, end)
            heapify(nums, 0, end-1)
            end -= 1
        
        return nums[-k]



if __name__ == "__main__":
    sol = Solution()
    print(sol.findKthLargest(nums=[3,2,1,5,6,4], k=2))
    print(sol.findKthLargest(nums=[3,2,3,1,2,4,5,5,6], k=4))