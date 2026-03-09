def triplet_sum(arr, target):
    """
    Given an array and a target, find all unique triplets in the array 
    which gives the sum of target.
    
    Time Complexity: O(N^2)
    Space Complexity: O(N) or O(log N) depending on sorting algorithm
    """
    
    # Sort the array to use the Two-Pointer technique
    arr.sort()
    
    n = len(arr)
    triplets = []
    
    for i in range(n - 2):
        # Skip duplicates for the first element
        if i > 0 and arr[i] == arr[i - 1]:
            continue
            
        left = i + 1
        right = n - 1
        
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            
            if current_sum == target:
                triplets.append([arr[i], arr[left], arr[right]])
                
                # Skip duplicates for the second element
                while left < right and arr[left] == arr[left + 1]:
                    left += 1
                
                # Skip duplicates for the third element
                while left < right and arr[right] == arr[right - 1]:
                    right -= 1
                    
                left += 1
                right -= 1
                
            elif current_sum < target:
                left += 1
            else:
                right -= 1
                
    return triplets

if __name__ == "__main__":
    test_arr = [-1, 0, 1, 2, -1, -4]
    target_sum = 0
    print(f"Triplets that sum to {target_sum}: {triplet_sum(test_arr, target_sum)}")
