# Implement the bucket sort algorithm 
def bucket_sort(arr):
    # Create an empty list to store the buckets
    buckets = [[] for _ in range(len(arr))]
    # Iterate through the input array and distribute elements into buckets
    for num in arr:
        index = int(num * len(arr))
        buckets[index].append(num)
    # Sort each bucket using insertion sort
    for bucket in buckets:
        bucket.sort()
    # Concatenate the sorted buckets to get the final sorted array
    sorted_arr = []
    for bucket in buckets:
        for num in bucket:
            sorted_arr.append(num)
    return sorted_arr

# Time complexity of bucket sort: 
# O(n^2) in worst case (if all elements are in one bucket)
# Average case O(n+k), where k is the number of buckets
# Space complexity of bucket sort: O(n) for buckets and sorted array

# Define an array of floating point numbers for testing bucket sort
arr = [0.1, 0.8, 0.3, 0.6, 0.5, 0.2, 0.9, 0.4, 0.7, 0.0]

# Perform bucket sort on the array of floating point numbers
sorted_arr = bucket_sort(arr)

# Display the original and sorted arrays
print("Original array:", arr)
print("Sorted array:", sorted_arr)

# Define a 2nd set of test cases
arr2 = [0.25, 0.75, 0.1, 0.9, 0.5, 0.6, 0.3, 0.8, 0.4, 0.7]

# Perform bucket sort on the 2nd array of floating point numbers
sorted_arr2 = bucket_sort(arr2)

# Display the original and sorted arrays
print("Original array:", arr2)
print("Sorted array:", sorted_arr2)