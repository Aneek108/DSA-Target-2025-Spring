def heapify_down_optimized(arr, n, i):

    largest = i  # Initialize largest as root

    while True:
        left = 2 * i + 1  # Left child index
        right = 2 * i + 2  # Right child index

        # Check if left child exists and is greater than root
        if left < n and arr[left] > arr[largest]:
            largest = left

        # Check if right child exists and is greater than largest so far
        if right < n and arr[right] > arr[largest]:
            largest = right

        # If no swap is needed, break early
        if largest == i:
            break

        # Swap and continue
        arr[i], arr[largest] = arr[largest], arr[i]
        i = largest

def build_max_heap_with_optimized_heapify_down(arr):

    n = len(arr)

    # Start from the last non-leaf node and move upward
    for i in range(n // 2 - 1, -1, -1):
        heapify_down_optimized(arr, n, i)

# Example usage
if __name__ == "__main__":
    arr = [3, 5, 9, 6, 8, 20, 10, 12, 18, 9]
    print("Original array:", arr)

    build_max_heap_with_optimized_heapify_down(arr)
    print("Max Heap:", arr)
