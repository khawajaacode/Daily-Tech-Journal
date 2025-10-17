def find_duplicates(nums):
    seen = set()
    duplicates = set()
    
    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    
    return list(duplicates)



nums = [1, 2, 3, 4, 5, 3, 2, 6, 7, 8, 1]
print(find_duplicates(nums))  # Output: [1, 2, 3]
