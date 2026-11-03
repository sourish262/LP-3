import random
import threading

# Maximum matrix size and number of threads
MAX = 4
MAX_THREAD = 4

# Initialize matrices
matA = [[0] * MAX for _ in range(MAX)]
matB = [[0] * MAX for _ in range(MAX)]
matC = [[0] * MAX for _ in range(MAX)]

step_i = 0
lock = threading.Lock()


def multi():
    """Thread worker function: evaluates one row of the resultant matrix matC."""
    global step_i

    # Thread-safe increment of the row counter
    with lock:
        i = step_i
        step_i += 1

    # Matrix multiplication logic for row i
    for j in range(MAX):
        for k in range(MAX):
            matC[i][j] += matA[i][k] * matB[k][j]


def print_matrix(matrix, name):
    print(f"\nMatrix {name}:")
    for row in matrix:
        print(" ".join(f"{val:2d}" for val in row))


def main():
    global matA, matB, matC

    # Generating random values (0 to 9) in matA and matB
    for i in range(MAX):
        for j in range(MAX):
            matA[i][j] = random.randint(0, 9)
            matB[i][j] = random.randint(0, 9)

    # Displaying input matrices
    print_matrix(matA, "A")
    print_matrix(matB, "B")

    # Declaring thread list
    threads = []

    # Creating four threads, each evaluating its own row
    for _ in range(MAX_THREAD):
        t = threading.Thread(target=multi)
        threads.append(t)
        t.start()

    # Joining and waiting for all threads to complete
    for t in threads:
        t.join()

    # Displaying the resultant matrix
    print_matrix(matC, "C (Multiplication of A and B)")


if __name__ == "__main__":
    main()
