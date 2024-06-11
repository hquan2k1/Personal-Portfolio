# Combining Quick and Bucket Sort to create a hybrid sorting algorithm
# Implement the hybrid sorting algorithm that uses quick sort for sorting buckets

# Define the quick sort function
# The pivot is a first element of the array
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Define the hybrid sort function
def hybrid_sort(arr):
    # Create an empty list to store the buckets
    buckets = [[] for _ in range(len(arr))]
    # Iterate through the input array and distribute elements into buckets
    for num in arr:
        index = int(num * len(arr))
        buckets[index].append(num)
    # Sort each bucket using quick sort
    for i in range(len(buckets)):
        quick_sort(buckets[i])
    # Concatenate the sorted buckets to get the final sorted array
    sorted_arr = []
    for bucket in buckets:
        for num in bucket:
            sorted_arr.append(num)
    return sorted_arr

# Analyze time complexity of the hybrid sorting algorithm
# Time complexity of quick sort: O(n log n) in average case, O(n^2) in worst case, O(n) in best case
# The best case will happen when the pivot is the median of the array, which will divide the array into two equal parts
# The worst case will happen when the pivot is the smallest or largest element, which will divide the array into one part and n-1 parts
# Time complexity of bucket sort: O(n^2) in worst case, O(n+k) in average case, O(n) in best case
# The best case will happen when the elements are uniformly distributed into buckets
# The worst case will happen when all elements are in one bucket
# Space complexity of quick sort: O(log n) for recursive calls
# Space complexity of bucket sort: O(n) for buckets and sorted array
# Time complexity of hybrid sort: O(n log n) in average case
# Space complexity of hybrid sort: O(n) for buckets and sorted array

# What input conditions allow the hybrid sorting algorithm to perform better than quick or bucket sort?
# The hybrid sorting algorithm performs better when the input array contains a wide range of values
# and the distribution of values is relatively uniform across the range.
# In such cases, the hybrid sorting algorithm can efficiently distribute elements into buckets
# and apply quick sort on each bucket to achieve a faster sorting time compared to quick or bucket sort alone.

# Define an array of floating point numbers for testing hybrid sort
arr = [0.1, 0.8, 0.3, 0.6, 0.5, 0.2, 0.9, 0.4, 0.7, 0.0]

# Perform hybrid sort on the array of floating point numbers
sorted_arr = hybrid_sort(arr)

# Display the original and sorted arrays
print("Original array:", arr)
print("Sorted array:", sorted_arr)