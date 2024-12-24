class Node:
    def __init__(self, val: int|float) -> None:
        self.val = val
        self.count: int = 1
        self.left: Node|None = None
        self.right: Node|None = None

class BinarySearchTree:
    def __init__(self) -> None:
        self.root: Node|None = None
    
    def is_leaf_node(node: Node) -> bool:
        return node.left is None and node.right is None

    def find_min(node: Node) -> Node:
        current = node
        while current.left is not None:
            current = current.left
        return current

    def find_max(node: Node) -> Node:
        current = node
        while current.right is not None:
            current = current.right
        return current

    def is_empty(self) -> bool:
        return self.root is None

    def insert(self, val: int|float) -> None:
        if self.root is None:
            self.root = Node(val)
            return

        current = self.root
        while True:
            if current.val == val:
                current.count += 1
                break
            elif val < current.val:
                if current.left is None:
                    current.left = Node(val)
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(val)
                    break
                current = current.right

    def search(self, val: int|float) -> Node|None:
        if self.root is None:
            return

        current = self.root
        while current is not None:
            if val == current.val:
                return current
            elif val < current.val:
                current = current.left
            else:
                current = current.right
        return None

    def delete(self, val: int|float) -> Node|None:
        """
        Deletes the node which consists the given value.
        
        ## Args
        `val`: The value of the node to be deleted

        ## Returns
        The root node of the modified BST.
        """
        if self.root is None: # If BST is empty
            return

        parent = None           # Variable which will hold the parent of the node to be deleted
        current = self.root     # Variable which will hold the node to be deleted
        is_left_child = False   # To determine if the current is left child of its parent
        
        # Finding the node
        while current is not None and current.val != val:
            if val < current.val:
                parent = current
                current = current.left
                is_left_child = True
            else:
                parent = current
                current = current.right
                is_left_child = False

        if current.count > 1:
            current.count -= 1
            return self.root

        # If leaf node
        if current.left is None and current.right is None:
            if parent is None: # Current is root
                self.root = None
            elif is_left_child:
                parent.left = None
            else:
                parent.right = None

        # If node has one child
        elif current.right is None: # Only left child exists
            if parent is None: # Current is root
                self.root = current.left
            elif is_left_child:
                parent.left = current.left
            else:
                parent.right = current.left

        elif current.left is None: # Only right child exists
            if parent is None: # Current is root
                self.root = current.right
            elif is_left_child:
                parent.left = current.right
            else:
                parent.right = current.right

        # If both childs are present
        else:
            # Find Inorder successor
            successor_parent = current
            successor = current.right

            while successor.left is not None:
                successor_parent = successor
                successor = successor.left
            
            # Update current's value with that of the successor's
            current.val = successor.val
            
            # Remove successor node
            if successor_parent == current: # Initial state did not change, While loop did not run
                successor_parent.right = successor.right
            else:
                successor_parent.left = successor.right

        return self.root
    
    def height(self) -> int:
        if self.root is None:
            return -1

        def height_helper(node: Node) -> int:
            if node is None:
                return -1

            height_left = height_helper(node.left)
            height_right = height_helper(node.right)

            return max(height_left, height_right) + 1

        return height_helper(self.root)

    def is_balanced(self) -> bool:

        def is_balanced_helper(node: Node) -> tuple[int, bool]:
            if node is None:
                return 0, True

            height_left, balanced_left = is_balanced_helper(node.left)
            height_right, balanced_right = is_balanced_helper(node.right)

            # Check if both left and right subtrees are balanced and the difference of their heights is at most 1.
            balanced = (balanced_left and balanced_right and abs(height_left - height_right) <= 1)

            return max(height_left, height_right) + 1, balanced

        return is_balanced_helper(self.root)[1]

if __name__ == "__main__":
    BST = BinarySearchTree()

    # Insert initial elements
    vals = [5, 2, 3, 4, 10, 1]
    for _ in vals:
        BST.insert(_)
    
    print(BST.is_balanced())
    print(BST.height())
    print()