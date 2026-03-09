def intersection(nums1, nums2):
    """
    Given two integer arrays nums1 and nums2, return an array of their intersection.
    Each element in the result must be unique and you may return the result in any order.
    
    Time Complexity: O(N + M)
    Space Complexity: O(min(N, M))
    """
    
    # We can use sets to find intersection efficiently
    set1 = set(nums1)
    set2 = set(nums2)
    
    return list(set1.intersection(set2))

if __name__ == "__main__":
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print(f"Intersection: {intersection(nums1, nums2)}")
