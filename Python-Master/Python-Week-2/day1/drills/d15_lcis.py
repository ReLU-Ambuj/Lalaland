def find_length_of_lcis(nums):
    """
    Given an unsorted array of integers nums, return the length of the longest 
    continuous increasing subsequence (i.e., subarray).
    The subsequence must be strictly increasing.
    
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    if not nums:
        return 0
        
    ans = 1
    anchor = 0
    
    for i in range(1, len(nums)):
        if nums[i-1] >= nums[i]:
            anchor = i
            
        ans = max(ans, i - anchor + 1)
        
    return ans

if __name__ == "__main__":
    nums = [1, 3, 5, 4, 7]
    print(f"Longest Continuous Increasing Subsequence length: {find_length_of_lcis(nums)}")
