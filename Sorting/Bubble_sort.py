# Bubble Sort

def bubble_sort(arr):

    n = len(arr)
    swapped = False
    i_counter = 0
    j_counter = 0

    for i in range(n-1):
        
        i_counter += 1
        for j in range(n-i-1):

            j_counter += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if swapped:
            swapped = False
        else:
            break

    return arr, i_counter, j_counter

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    arr.reverse()
    print(bubble_sort(arr))