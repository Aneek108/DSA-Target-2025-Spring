def heapify_up_optimized(arr, i):

    current = arr[i]  # Save the current value to minimize swaps
    parent = (i - 1) // 2  # Calculate parent index

    # Continue heapifying while the node is not the root and the node is greater than its parent
    while i > 0 and current > arr[parent]:
        arr[i] = arr[parent]  # Move parent down
        i = parent  # Move up to the parent index
        parent = (i - 1) // 2

    arr[i] = current  # Place the saved value in its final position

def build_max_heap_with_optimized_heapify_up(arr):

    n = len(arr)

    # Start from the first element and heapify up for each
    for i in range(1, n):
        heapify_up_optimized(arr, i)

# Example usage
if __name__ == "__main__":
    arr = [3, 5, 9, 6, 8, 20, 10, 12, 18, 9]
    print("Original array:", arr)

    build_max_heap_with_optimized_heapify_up(arr)
    print("Max Heap:", arr)
