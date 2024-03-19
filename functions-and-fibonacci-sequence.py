def generate_fibonacci_sequence(n):
    # Initialize the Fibonacci sequence with the first two terms
    fibonacci_sequence = [0, 1]  

    # Generate the Fibonacci sequence up to the nth term
    for i in range(2, n):
        # Calculate the next term by adding the last two terms
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        # Append the next term to the sequence
        fibonacci_sequence.append(next_term)
    return fibonacci_sequence

def main():
    try:
        # Prompt the user to input the number of terms
        n = int(input("Enter the number of terms for the Fibonacci sequence: "))
        
        # Check if the input is a positive integer
        if n <= 0:
            print("Please enter a positive integer.")
            return
        
        # Generate the Fibonacci sequence
        fibonacci_sequence = generate_fibonacci_sequence(n)
        
        # Print the generated Fibonacci sequence
        print("The Fibonacci sequence up to term", n, "is:", fibonacci_sequence)
    
    # Handle the case where the input is not a valid integer
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
