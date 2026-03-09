def majority_element(nums):
    """
    Given an array nums of size n, return the majority element.
    The majority element is the element that appears more than ⌊n / 2⌋ times.
    You may assume that the majority element always exists in the array.
    
    Uses Boyer-Moore Voting Algorithm.
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate

if __name__ == "__main__":
    nums = [2, 2, 1, 1, 1, 2, 2]
    print(f"Majority Element: {majority_element(nums)}")
