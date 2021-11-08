def bubble_sort(nums):
    swap = True
    while swap:
        swap = False
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                swap = True
                nums[i], nums[i+1] = nums[i+1], nums[i]
    
    return nums


def selection_sort(nums):
    for i in range(len(nums)):
        min_index, curr_min = i, nums[i]
        for j in range(i+1, len(nums)):
            if nums[j] < curr_min:
                min_index, curr_min = j, nums[j]
        nums[i], nums[min_index] = nums[min_index], nums[i]

    return nums


def insertion_sort(nums):
    for i in range(1, len(nums)):
        current = nums[i]
        for j in range(i-1, -1, -1):
            if nums[j] > current:
                nums[j+1] = nums[j]
                nums[j] = current
            else: break
        
    return nums


def heap_sort(nums):
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
        
    for end in range(len(nums)-1, 0, -1):
        swap(nums, 0, end)
        heapify(nums, 0, end-1)
    
    return nums


def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)

        l, r = 0, 0
        for i in range(len(nums)):
            if l < len(left) and r < len(right):
                if left[l] < right[r]: nums[i] = left[l] ; l += 1
                else: nums[i] = right[r] ; r += 1
            elif l < len(left): nums[i] = left[l] ; l += 1
            else: nums[i] = right[r] ; r += 1
        
    return nums


def quick_sort(nums):
    def qs_helper(nums, left, right):
        if right - left >= 1:
            i, j = left, right
            pivot = nums[left]
            while i != j:
                while nums[j] >= pivot and i < j: j -= 1
                while nums[i] <= pivot and i < j: i += 1
                if i < j: nums[i], nums[j] = nums[j], nums[i]
            nums[left], nums[i] = nums[i], nums[left]

            qs_helper(nums, left, i-1)
            qs_helper(nums, i+1, right)
    
    qs_helper(nums, 0, len(nums)-1)
    return nums



if __name__ == "__main__":
    print(bubble_sort([5, 2, 1, 8, 4]))
    print(selection_sort([5, 2, 1, 8, 4]))
    print(insertion_sort([5, 2, 1, 8, 4]))
    print(heap_sort([5, 2, 1, 8, 4]))
    print(merge_sort([5, 2, 1, 8, 4]))
    print(quick_sort([5, 2, 1, 8, 4]))