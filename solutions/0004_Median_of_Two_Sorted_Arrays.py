from utils import timer

class Solution:
    # Solution 1: Merge & Sort
    # @timer
    # def findMedianSortedArrays(self, nums1, nums2):
    #     num = nums1 + nums2
    #     num.sort()
    #     l = len(num)
    #     if l % 2 == 0: return (num[l // 2 - 1] + num[l // 2]) / 2
    #     else: return num[l // 2]

    # Solution 2: Binary Search
    @timer
    def findMedianSortedArrays(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        if m > n: return self.findMedianSortedArrays(nums2, nums1)
        l = m + n
        half = l // 2
        if l % 2 == 1: half += 1
        
        left, right = 0, m-1
        nums1, nums2 = nums1 + [float("infinity")], nums2 + [float("infinity")]
        while True:
            mid1 = (left + right) // 2
            mid2 =  half - mid1 - 2
            if mid1 >= 0 and mid2 >= 0:
                if nums1[mid1] <= nums2[mid2+1] and nums2[mid2] <= nums1[mid1+1]: break
                elif nums1[mid1] > nums2[mid2+1]: right = mid1 - 1
                else: left = mid1 + 1
            elif mid1 < 0:
                if nums2[mid2] <= nums1[mid1+1]: break
                else: left = mid1 + 1
            elif mid2 < 0:
                if nums1[mid1] <= nums2[mid2+1]: break
                else: right = mid1 - 1

        if l % 2 == 1:
            if mid1 >= 0 and mid2 >= 0: return max(nums1[mid1], nums2[mid2])
            elif mid1 < 0: return nums2[mid2]
            else: return nums1[mid1]
        else:
            if mid1 >= 0 and mid2 >= 0:
                median1 = max(nums1[mid1], nums2[mid2])
                median2 = min(nums1[mid1+1], nums2[mid2+1])
                
            elif mid1 < 0:
                median1 = nums2[mid2]
                median2 = min(nums1[0], nums2[mid2+1])
            else:
                median1 = nums1[mid1]
                median2 = min(nums1[mid1+1], nums2[0])
            return (median1 + median2) / 2


if __name__ == "__main__":
    sol = Solution()
    print(sol.findMedianSortedArrays([3,4,5,6,7], [1,2]))
    print(sol.findMedianSortedArrays([1,2,3,4,6,7], [5]))
    print(sol.findMedianSortedArrays([2,3,4,5,6], [1]))
    print(sol.findMedianSortedArrays([3], [-2,-1]))
    print(sol.findMedianSortedArrays(nums1=[1,3], nums2=[2]))
    print(sol.findMedianSortedArrays(nums1=[1,2], nums2=[3,4]))
    print(sol.findMedianSortedArrays(nums1=[0,0], nums2=[0,0]))
    print(sol.findMedianSortedArrays(nums1=[], nums2=[1]))
    print(sol.findMedianSortedArrays(nums1=[2], nums2=[]))
