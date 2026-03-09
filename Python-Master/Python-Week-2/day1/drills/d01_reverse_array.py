def reverse_array(arr):
    """
    Reverses an array in-place.
    
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    left, right = 0, len(arr) - 1
    
    while left < right:
        # Swap elements at left and right indices
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr

if __name__ == "__main__":
    test_arr = [1, 2, 3, 4, 5]
    print(f"Original: {test_arr}")
    reverse_array(test_arr)
    print(f"Reversed: {test_arr}")
