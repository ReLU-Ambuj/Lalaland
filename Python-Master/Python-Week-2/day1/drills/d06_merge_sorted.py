def merge(nums1, m, nums2, n):
    """
    Given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
    and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
    
    Merge nums1 and nums2 into a single array sorted in non-decreasing order.
    Do this in-place in nums1 (which has a length of m + n).
    
    Time Complexity: O(m + n)
    Space Complexity: O(1)
    """
    
    # Start pointers from the end of both arrays
    p1 = m - 1
    p2 = n - 1
    
    # Pointer for placing the largest element
    p_merge = m + n - 1
    
    # While there are still elements to consider in nums2
    while p2 >= 0:
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p_merge] = nums1[p1]
            p1 -= 1
        else:
            nums1[p_merge] = nums2[p2]
            p2 -= 1
        p_merge -= 1

if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    merge(nums1, m, nums2, n)
    print(f"Merged Array: {nums1}")
