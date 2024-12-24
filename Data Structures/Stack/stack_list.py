class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1]

    def is_empty(self) -> bool:
        return len(self.stack) == 0

    def size(self) -> int:
        return len(self.stack)
    
print(int(5).to_bytes())
print(Stack().is_empty())

stk = Stack()

while True:
    print("""
        MENU:
          1. Push
          2. Pop
          3. Peek
          4. Is Empty
          5. Size
          6. Exit
    """)

    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            val = int(input("Enter the value to push: "))
            stk.push(val)
        case 2:
            stk.pop()
        case 3:
            print(stk.peek())
        case 4:
            print(stk.is_empty())
        case 5:
            print(stk.size())
        case 6:
            break
        case _:
            print("Invalid choice")
    print(stk.stack)