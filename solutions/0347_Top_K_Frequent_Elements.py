import heapq
from utils import timer

class Solution:

    # Solution 1: Count & Sort
    # @timer
    # def topKFrequent(self, nums, k):
    #     counter = {}
    #     for n in nums:
    #         counter[n] = counter.get(n, 0) + 1
    #     sorted_counter = sorted(list(counter.items()), key=lambda x: -x[1])

    #     return [i[0] for i in sorted_counter[:k]]

    # Solution 2: Heap
    # @timer
    # def topKFrequent(self, nums, k):
    #     counter = {}
    #     for n in nums:
    #         counter[n] = counter.get(n, 0) + 1
        
    #     return heapq.nlargest(k, counter.keys(), key=lambda x: counter[x])

    # Solution 3: Quick Select
    @timer
    def topKFrequent(self, nums, k):
        def quick_selection(counter, left, right):
            if right - left >= 1:
                i, j = left, right
                pivot = counter[left][1]
                while i != j:
                    while counter[j][1] >= pivot and i < j: j -= 1
                    while counter[i][1] <= pivot and i < j: i += 1
                    if i < j: counter[i], counter[j] = counter[j], counter[i]
                counter[left], counter[i] = counter[i], counter[left]

                return i
            else: return left

        counter = {}
        for n in nums:
            counter[n] = counter.get(n, 0) + 1
        counter = list(counter.items())

        l, r = 0, len(counter) - 1
        while l <= r:
            pivot = quick_selection(counter, l, r)
            largest_k = len(counter) - pivot
            if largest_k == k: return [x[0] for x in counter[pivot:]]
            elif largest_k < k: r = pivot - 1
            else: l = pivot + 1




if __name__ == "__main__":
    sol = Solution()
    print(sol.topKFrequent(nums=[1,1,1,2,2,3], k=2))
    print(sol.topKFrequent(nums=[1], k=1))

        
