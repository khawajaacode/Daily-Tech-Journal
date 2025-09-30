def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid  # return index if found
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # return -1 if not found


# Example usage
arr = [1, 3, 5, 7, 9, 11]
target = 7
result = binary_search(arr, target)

print("Found at index:", result if result != -1 else "Not Found")
