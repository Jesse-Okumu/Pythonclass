def calculate_factorial(n):
    """
    Calculate the factorial of a given positive integer.
    """
    # Initialize factorial to 1 (since 0! = 1)
    factorial = 1

    # Use a loop to multiply numbers from 1 to n
    for i in range(1, n + 1):
        factorial *= i

    return factorial


def get_positive_integer():
    """
    Prompt the user for a positive integer and validate the input.
    """
    while True:
        try:
            # Ask the user for input
            num = int(input("Enter a positive integer to calculate its factorial: "))

            # Ensure the number is non-negative
            if num < 0:
                print("Please enter a positive integer.")
            else:
                return num

        except ValueError:
            print("Invalid input! Please enter a valid positive integer.")


def main():
    """
    Main function to execute the factorial calculation program.
    """
    print("Welcome to the Factorial Calculation Program!")

    # Get a valid positive integer from the user
    number = get_positive_integer()

    # Calculate the factorial
    result = calculate_factorial(number)

    # Display the result
    print(f"The factorial of {number} is: {result}")


# Ensure the script runs only when executed directly
if __name__ == "__main__":
    main()
