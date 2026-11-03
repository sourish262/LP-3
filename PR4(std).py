def knapSack2D(W, wt, val, n):
    # Create a 2D table of dimension (n + 1) x (W + 1) initialized to 0
    K = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Build table K[][] in bottom-up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    # Trace back to find the items included in the knapsack
    res = K[n][W]
    print(f"Maximum possible value = {res}")

    w = W
    selected_items = []
    for i in range(n, 0, -1):
        if res <= 0:
            break
        # If the result comes from K[i-1][w], the item was not included
        if res == K[i - 1][w]:
            continue
        else:
            # Item is included
            selected_items.append(i)
            res -= val[i - 1]
            w -= wt[i - 1]

    print("Selected items (1-indexed):", selected_items[::-1])
    return K[n][W]


# Driver code with manual example
if __name__ == "__main__":
    val = [3, 4, 5, 6]
    wt = [2, 3, 4, 5]
    W = 5
    n = len(val)

    knapSack2D(W, wt, val, n)
