def union(nums1, nums2):
    """
    Given two arrays a and b, find their union.
    The union of two arrays can be defined as the common and distinct elements in the two arrays.
    
    Time Complexity: O(N + M)
    Space Complexity: O(N + M)
    """
    
    # Using sets to handle duplicates automatically
    union_set = set(nums1).union(set(nums2))
    
    return list(union_set)

if __name__ == "__main__":
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [1, 2, 3]
    print(f"Union: {union(nums1, nums2)}")
