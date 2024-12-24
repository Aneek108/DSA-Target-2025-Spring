# Max-Heap Implementation
class Heap:
    def __init__(self) -> None:
        self.heap: list = []

    def heapify_down(self, i: int, n: int) -> None:
        largest = i

        while True:
            left = 2 * i + 1  # Left child index
            right = 2 * i + 2  # Right child index

            if left < n and self.heap[left] > self.heap[largest]:
                largest = left
            if right < n and self.heap[right] > self.heap[largest]:
                largest = right
            if largest == i: # Early break
                break

            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            i = largest

    def heapify_up(self, i: int) -> None:
        current = self.heap[i]
        parent = (i - 1) // 2

        while i > 0 and current > self.heap[parent]:
            self.heap[i] = self.heap[parent]
            i = parent
            parent = (i - 1) // 2
    
        self.heap[i] = current

    def peek(self) -> int|float|None:
        if len(self.heap) == 0:
            return
        return self.heap[0]
    
    def delete(self, i: int) -> int|float:
        self.heap[i], self.heap[-1] = self.heap[-1], self.heap[i]
        deleted_val = self.heap.pop()
        self.heapify_down(i, len(self.heap))
        return deleted_val

    def insert(self, value: int|float) -> None:
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def search(self, value: int|float) -> int:
        for i in range(len(self.heap) - 1):
            if self.heap[i] == value:
                return i
        return -1




