arr = [5, 2, 9, 1, 7]

# Maximum
max_val = arr[0]
for num in arr:
    if num > max_val:
        max_val = num

# Minimum
min_val = arr[0]
for num in arr:
    if num < min_val:
        min_val = num

print("Maximum:", max_val)
print("Minimum:", min_val)
