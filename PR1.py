# ==========================================
# Method 1: Non-Recursive (Iterative) Approach
# ==========================================
def fibonacci_non_recursive():
    nterms = int(input("How many terms? "))

    # First two terms
    n1, n2 = 0, 1
    count = 0

    # Check if the number of terms is valid
    if nterms <= 0:
        print("Please enter a positive integer")
    elif nterms == 1:
        print(f"Fibonacci sequence upto {nterms}:")
        print(n1)
    else:
        print("Fibonacci sequence:")
        while count < nterms:
            print(n1)
            nth = n1 + n2
            # Update values
            n1 = n2
            n2 = nth
            count += 1


# ==========================================
# Method 2: Recursive Approach
# ==========================================
def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo(n - 1) + recur_fibo(n - 2)


def fibonacci_recursive():
    nterms = int(input("How many terms? "))

    # Check if the number of terms is valid
    if nterms <= 0:
        print("Please enter a positive integer")
    else:
        print("Fibonacci sequence:")
        for i in range(nterms):
            print(recur_fibo(i))


# Driver code to test both
if __name__ == "__main__":
    print("--- Non-Recursive Method ---")
    fibonacci_non_recursive()

    print("\n--- Recursive Method ---")
    fibonacci_recursive()
