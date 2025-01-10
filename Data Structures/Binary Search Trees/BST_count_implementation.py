from Binary_Search_Tree import BinarySearchTree, Node

class Count_Node(Node):
    def __init__(self, val: int|float) -> None:
        super().__init__(val)
        self.count = 1

class Count_BST(BinarySearchTree):
    def __init__(self) -> None:
        self.root: Count_Node|None = None

    def insert(self, val: int|float) -> None:
        if self.root is None:
            self.root = Count_Node(val)
            return

        current = self.root
        while True:
            if val < current.val:
                if current.left is None:
                    current.left = Count_Node(val)
                    return
                current = current.left
            elif val > current.val:
                if current.right is None:
                    current.right = Count_Node(val)
                    return
                current = current.right
            else: # If value already exists
                current.count += 1
                return

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
        
        # If node not found
        if current is None:
            return self.root
        
        # If count is greater than 1, decrement count and return
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
        if current.right is None: # Only left child exists
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
        # Find Inorder successor
        successor_parent = current
        successor = current.right

        while successor.left is not None:
            successor_parent = successor
            successor = successor.left
        
        # Update current's value with that of the successor's
        current.val = successor.val
        
        # Remove successor node
        if successor_parent == current: # Initial state did not change,i.e., While loop did not run
            successor_parent.right = successor.right
        else:
            successor_parent.left = successor.right

        return self.root

    def intensive_node_count(self) -> int:
        
        def intensive_node_count_helper(node: Count_Node) -> int:
            if node is None:
                return 0
            return node.count + intensive_node_count_helper(node.left) + intensive_node_count_helper(node.right)
        
        return intensive_node_count_helper(self.root)

if __name__ == "__main__":
    BST = Count_BST()

    # Insert initial elements
    vals = [5, 2, 3, 4, 10, 1, 2]
    for _ in vals:
        BST.insert(_)
    
    print(BST.is_balanced())
    print(BST.height())
    print(BST.inorder_traversal())
    BST.delete(5)
    print(BST.inorder_traversal())
    print(BST.node_count())
    print(BST.intensive_node_count())