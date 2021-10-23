from utils import timer

class Solution:

    # Solution 1: Combine & Sort
    # @timer
    # def merge(self, nums1, m, nums2, n):
    #     """
    #     Do not return anything, modify nums1 in-place instead.
    #     """
    #     for n in nums2:
    #         nums1[m] = n
    #         m+=1
    #     nums1.sort()

    # Solution 2: Two Pointers
    @timer
    def merge(self, nums1, m, nums2, n):
        pos = m + n - 1
        m -= 1 ; n -=1
        while m >= 0 and n >= 0:
            if nums1[m] <= nums2[n]:
                nums1[pos] = nums2[n] ; n -= 1
            else:
                nums1[pos] = nums1[m] ; m -= 1
            pos -= 1
        if m < 0:
            nums1[:pos+1] = nums2[:n+1]




if __name__ == "__main__":
    sol = Solution()
    sol.merge(nums1=[1,2,3,0,0,0], m=3, nums2=[2,5,6], n=3)
    sol.merge(nums1=[1], m=1, nums2=[], n=0)
    sol.merge(nums1=[0], m=0, nums2=[1], n=1)
        