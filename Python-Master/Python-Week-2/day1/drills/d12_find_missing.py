def find_missing_number(nums):
    """
    Given an array nums containing n distinct numbers in the range [0, n], 
    return the only number in the range that is missing from the array.
    
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    
    n = len(nums)
    expected_sum = (n * (n + 1)) // 2
    actual_sum = sum(nums)
    
    return expected_sum - actual_sum

if __name__ == "__main__":
    nums = [3, 0, 1]
    print(f"Missing number in {nums} is: {find_missing_number(nums)}")
