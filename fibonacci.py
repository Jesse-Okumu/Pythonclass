# A program to calculate the Fibonacci sequence up to the n-th term provided by the user

def fibonacci(n):
    """Generates the Fibonacci sequence up to the n-th term."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    # Generate Fibonacci sequence recursively
    fib_seq = fibonacci(n - 1)
    fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq

def main():
    """Main function to interact with the user and display the Fibonacci sequence."""
    print("Welcome to the Fibonacci Sequence Program!")

    # Get user input and validate it
    while True:
        try:
            n = int(input("How many Fibonacci terms would you like to generate? "))
            if n <= 0:
                print("Please enter a positive integer greater than 0.")
            else:
                break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

    # Generate and display the Fibonacci sequence
    fibonacci_sequence = fibonacci(n)
    print(f"\nThe first {n} terms of the Fibonacci sequence are:")
    print(fibonacci_sequence)

# Ensures the script runs only when executed directly, not when imported
if __name__ == "__main__":
    main()
