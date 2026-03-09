def two_sum_sorted(arr, target):
    """
    Finds two numbers such that they add up to a specific target number.
    Returns the indices of the two numbers counting from 1 (1-indexed).
    Assuming there is exactly one solution.
    
    Uses Two Pointers.
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    left, right = 0, len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1  # Need a larger sum
        else:
            right -= 1 # Need a smaller sum
            
    return []

if __name__ == "__main__":
    test_arr = [2, 7, 11, 15]
    target = 9
    print(f"Indices: {two_sum_sorted(test_arr, target)}")
