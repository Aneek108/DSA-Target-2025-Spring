class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.next: Node = None
        self.prev: Node = None

class Stack:
    def __init__(self):
        self.top: Node = None

    def is_empty(self) -> bool:
        return self.top is None

    def push(self, val: int) -> None:
        if self.is_empty():
            self.top = Node(val)
            return
        
        self.top.next = Node(val)
        self.top.next.prev = self.top
        self.top = self.top.next

    def pop(self) -> Node:
        if self.is_empty():
            return
        
        del_val = self.top.data
        self.top = self.top.prev
        del_node = self.top.next
        del(del_node)
        return del_val
    
    def peek(self) -> int:
        return self.top.data
    
    def size(self) -> int:
        size = 0
        current = self.top
        while current is not None:
            size += 1
            current = current.prev
        return size
    
    def traverse(self) -> None:
        current = self.top
        print("Top", end="-> ")
        while current is not None:
            print(current.data, end=" ")
            current = current.prev
        print()

stk = Stack()

while True:
    print("""
        MENU:
          1. Push
          2. Pop
          3. Peek
          4. Is Empty
          5. Size
          6. Traverse
          7. Exit
    """)

    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            val = int(input("Enter the value to push: "))
            stk.push(val)
        case 2:
            print("Popped", stk.pop())
        case 3:
            print(stk.peek())
        case 4:
            print(stk.is_empty())
        case 5:
            print(stk.size())
        case 6:
            stk.traverse()
        case 7:
            break
        case _:
            print("Invalid choice")