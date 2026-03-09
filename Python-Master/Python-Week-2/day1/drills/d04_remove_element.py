def remove_element(nums, val):
    """
    Given an array nums and a value val, remove all instances of that value in-place 
    and return the new length.
    
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    
    # 'slow' pointer keeps track of where to place the next valid (non-val) element
    slow = 0
    
    for fast in range(len(nums)):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
            
    return slow

if __name__ == "__main__":
    test_arr = [3, 2, 2, 3]
    val_to_remove = 3
    new_length = remove_element(test_arr, val_to_remove)
    print(f"New Length: {new_length}")
    print(f"Modified Array: {test_arr[:new_length]}")
