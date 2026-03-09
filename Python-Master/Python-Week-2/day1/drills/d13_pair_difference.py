def pair_difference(arr, diff):
    """
    Given a sorted array and a target difference diff, find a pair such that 
    their absolute difference is equal to diff.
    
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    
    # We use two pointers starting from the same end but at different speeds
    i = 0
    j = 1
    
    n = len(arr)
    
    while i < n and j < n:
        if i != j and abs(arr[j] - arr[i]) == diff:
            return (arr[i], arr[j])
        elif arr[j] - arr[i] < diff:
            # Difference is too small, increase the larger number
            j += 1
        else:
            # Difference is too large, increase the smaller number
            i += 1
            
    return None

if __name__ == "__main__":
    sorted_arr = [1, 8, 30, 40, 100]
    target_diff = 60
    # Note: array must be sorted! 
    # [1, 8, 30, 40, 100] is already sorted.
    res = pair_difference(sorted_arr, target_diff)
    if res:
        print(f"Pair with diff {target_diff}: {res}")
    else:
        print("No such pair found.")
