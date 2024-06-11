# Define a function to perform interpolation search on a sorted array of integers
# The function should return the index of the target value if it is found in the array
# Otherwise, the function should return -1
def interpolation_search(arr, target):
    # Define the low and high indices of the array
    low = 0
    high = len(arr) - 1
    # Continue searching while the target value is within the array bounds
    while low <= high and target >= arr[low] and target <= arr[high]:
        # Calculate the position of the target value using interpolation
        pos = low + (high - low) // (arr[high] - arr[low]) * (target - arr[low])
        # If the target value is found at the calculated position, return the index
        if arr[pos] == target:
            return pos
        # If the target value is greater than the value at the calculated position
        # Update the low index to search the right subarray
        elif arr[pos] < target:
            low = pos + 1
        # If the target value is less than the value at the calculated position
        # Update the high index to search the left subarray
        else:
            high = pos - 1
    # If the target value is not found in the array, return -1
    return -1

# Define a sorted array of integers for testing interpolation search
arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Test interpolation search with target values
target1 = 30
target2 = 70
target3 = 55

# Perform interpolation search on the array with the target values
index1 = interpolation_search(arr, target1)
index2 = interpolation_search(arr, target2)
index3 = interpolation_search(arr, target3)

# Print the sorted array for reference
print("Sorted array:", arr)

# Display the results of interpolation search
print(f"Target value {target1} found at index {index1}")
print(f"Target value {target2} found at index {index2}")
print(f"Target value {target3} found at index {index3}")

# Define 2nd set of test cases
arr2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Test interpolation search with target values
target4 = 6
target5 = 14
target6 = 9

# Perform interpolation search on the 2nd array with the target values
index4 = interpolation_search(arr2, target4)
index5 = interpolation_search(arr2, target5)
index6 = interpolation_search(arr2, target6)

# Print the sorted array for reference
print("Sorted array:", arr2)

# Display the results of interpolation search
print(f"Target value {target4} found at index {index4}")
print(f"Target value {target5} found at index {index5}")
print(f"Target value {target6} found at index {index6}")