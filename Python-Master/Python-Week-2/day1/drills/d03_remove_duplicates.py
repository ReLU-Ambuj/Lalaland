def remove_duplicates(nums):
    """
    Given a sorted array, remove the duplicates in-place such that each element appears only once.
    Returns the new length of the array.
    Do not allocate extra space for another array.
    """
    if not nums:
        return 0
        
    # 'slow' pointer tracks the position of the last unique element found
    slow = 0
    
    # 'fast' pointer scans through the array
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
            
    return slow + 1

if __name__ == "__main__":
    test_arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    new_length = remove_duplicates(test_arr)
    print(f"New Length: {new_length}")
    print(f"Modified Array: {test_arr[:new_length]}")
