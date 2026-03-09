def sorted_squares(nums):
    """
    Given an integer array nums sorted in non-decreasing order, return an array of 
    the squares of each number sorted in non-decreasing order.
    
    Time Complexity: O(N)
    Space Complexity: O(N) to store the result
    """
    
    n = len(nums)
    result = [0] * n
    
    left, right = 0, n - 1
    
    # Fill the result array from right to left
    for i in range(n - 1, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            result[i] = nums[left] * nums[left]
            left += 1
        else:
            result[i] = nums[right] * nums[right]
            right -= 1
            
    return result

if __name__ == "__main__":
    test_arr = [-4, -1, 0, 3, 10]
    print(f"Squares sorted: {sorted_squares(test_arr)}")
