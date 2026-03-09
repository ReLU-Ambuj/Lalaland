def squares_sorted_basic(nums):
    """
    Given an integer array nums sorted in non-decreasing order, return an array of 
    the squares of each number sorted in non-decreasing order.
    
    This is the O(N log N) approach (square then sort).
    See d08_sorted_squares.py for the O(N) Two-Pointer approach.
    """
    
    # Square all numbers in place
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2
        
    # Python's built-in sort (Timsort) takes O(N log N) time
    nums.sort()
    
    return nums

if __name__ == "__main__":
    test_arr = [-4, -1, 0, 3, 10]
    print(f"Squares sorted (O(N log N) approach): {squares_sorted_basic(test_arr)}")
