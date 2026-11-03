# Structure for an item containing value and weight
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight


def fractionalKnapsack(W, arr):
    # Sorting items in decreasing order of value-to-weight ratio
    arr.sort(key=lambda x: (x.value / x.weight), reverse=True)

    # Result (total value accumulated in knapsack)
    finalvalue = 0.0

    # Looping through all items
    for item in arr:
        # If adding the entire item does not exceed capacity, take it completely
        if item.weight <= W:
            W -= item.weight
            finalvalue += item.value
        # If full item cannot be added, take the remaining fractional part
        else:
            finalvalue += item.value * (W / item.weight)
            break

    # Returning maximum profit/value
    return finalvalue


# Driver Code
if __name__ == "__main__":
    # Capacity of knapsack
    W = 40

    # List of items with (value, weight)
    arr = [
        Item(60, 10),
        Item(100, 20),
        Item(120, 30)
    ]

    # Function call
    max_val = fractionalKnapsack(W, arr)
    print("Maximum value we can obtain =", max_val)
