def move_zeroes(nums):
    """
    Given an integer array nums, move all 0's to the end of it while 
    maintaining the relative order of the non-zero elements.
    
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    
    # Pointer for where the next non-zero element should go
    insert_pos = 0
    
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[insert_pos], nums[i] = nums[i], nums[insert_pos]
            insert_pos += 1

if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    move_zeroes(nums)
    print(f"Moved Zeroes: {nums}")
