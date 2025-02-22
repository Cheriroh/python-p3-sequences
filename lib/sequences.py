def print_fibonacci(length):
    # Initialize the Fibonacci sequence
    
    
    # Edge cases
    if length == 0:
        print('[]') # Print empty list for length 0
        return
    
    fib_sequence = []

    if length >= 1:
        fib_sequence.append(0)
          # The first Fibonacci number
    if length >= 2:
        fib_sequence.append(1)  # The second Fibonacci number

    # Generate the Fibonacci sequence for lengths greater than 2
    for i in range(2, length):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)

    # Print the Fibonacci sequence as a list (this will print to stdout)
    print(fib_sequence)
