# Creating Fibonacci sequence using recursion
def fibonacci(n):
    # Base case
    if n <= 1:
        return n
    # Recursive call
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter the number of terms: "))
# Check if the number of terms is valid
if n <= 0:
    print("Please enter a positive integer")
# Display the Fibonacci sequence sequentially
else:
    print("Fibonacci sequence:", end=" ")
    for i in range(n):
        print(fibonacci(i), end=" ")