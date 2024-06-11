# Creating Fibonacci sequence using recursion
def fibonacci(n):
    # Base case
    if n <= 1:
        return n
    # Recursive call
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
# Fibonacci function using dynamic programming
# Dynamic programming is the concept of storing intermediate results to avoid redundant calculations
# The time complexity of the dynamic programming approach is O(n)
# The space complexity of the dynamic programming approach is O(n)
# The recurrence relation for the Fibonacci sequence is F(n) = F(n-1) + F(n-2), where F(0) = 0 and F(1) = 1, a = 1, b = 1, T(n) = 2T(n-1) + 1
def fibonacci_dp(n):
    # Initialize the first two Fibonacci numbers
    fib = [0, 1]
    # Calculate the Fibonacci sequence up to the nth term
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]

n = int(input("Enter the number of terms: "))
# Check if the number of terms is valid
if n <= 0:
    print("Please enter a positive integer")
# Display the Fibonacci sequence sequentially
else:
    print("Fibonacci sequence:", end=" ")
    for i in range(n):
        print(fibonacci_dp(i), end=" ")