from collections import deque

class Node:
    def __init__(self, val: int | float) -> None:
        self.val = val
        self.left: Node | None = None
        self.right: Node | None = None

class BinaryTree:
    def __init__(self) -> None:
        self.root: Node | None = None

    def is_leaf_node(node: Node) -> bool:
        return node.left is None and node.right is None

    def is_empty(self) -> bool:
        return self.root is None

    def deepest_node(self) -> Node | None:
        if self.root is None:
            return None

        queue = deque([self.root])
        while queue:
            current = queue.popleft()

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return current

    def level_order_traversal(root: Node) -> list[int | float]:
        if not root:
            return

        traverse = []

        queue = deque([root])  # Initialize the queue with the root
        while queue:
            current = queue.popleft()  # Dequeue the front node
            traverse.append(current.val)  # Process the current node

            # Enqueue the left and right children (if they exist)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return [node.val for node in traverse]

    def reverse_level_order_traversal(root: Node) -> list[int | float]:
        if not root:
            return []

        queue = deque([root])
        stack = []

        while queue:
            current = queue.popleft()
            stack.append(current)

            # Enqueue right before left to reverse order
            if current.right:
                queue.append(current.right)
            if current.left:
                queue.append(current.left)

        stack.reverse()
        return [node.val for node in stack]

    def level_order_grouping(root: Node) -> list[list[int | float]]:
        if not root:
            return []

        queue = deque([root])
        result = []

        while queue:
            level_size = len(queue)  # Number of nodes at the current level
            level_nodes = []

            for _ in range(level_size):
                current = queue.popleft()
                level_nodes.append(current.val)

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

            result.append(level_nodes)

        return result

    def inorder_traversal(self) -> list[int | float]:
        traverse = []

        def inorder_traversal_helper(node: Node) -> None:
            if node is None:
                return

            inorder_traversal_helper(node.left)
            traverse.append(node.val)
            inorder_traversal_helper(node.right)

        inorder_traversal_helper(self.root)
        return traverse

    def preorder_traversal(self) -> list[int | float]:
        traverse = []

        def preorder_traversal_helper(node: Node) -> None:
            if node is None:
                return

            traverse.append(node.val)
            preorder_traversal_helper(node.left)
            preorder_traversal_helper(node.right)

        preorder_traversal_helper(self.root)
        return traverse

    def postorder_traversal(self) -> list[int | float]:
        traverse = []

        def postorder_traversal_helper(node: Node) -> None:
            if node is None:
                return

            postorder_traversal_helper(node.left)
            postorder_traversal_helper(node.right)
            traverse.append(node.val)

        postorder_traversal_helper(self.root)
        return traverse

    def insert(self, val: int | float) -> None:
        """Inserts a new node with the given value into the binary tree using BFS."""
        if self.root is None:
            self.root = Node(val)
            return

        queue = deque([self.root])
        while queue:
            current = queue.popleft()

            if current.left is None:
                current.left = Node(val)
                return
            else:
                queue.append(current.left)

            if current.right is None:
                current.right = Node(val)
                return
            else:
                queue.append(current.right)

    def search(self, val: int | float) -> Node | None:
        """Searches for a node with the given value in the binary tree using BFS."""
        if self.root is None:
            return None

        queue = deque([self.root])
        while queue:
            current = queue.popleft()

            if current.val == val:
                return current

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return None

    def delete(self, val: int | float) -> Node:
        """Deletes a node with the given value from the binary tree using BFS, and returns the root node of the updated tree."""
        if self.root is None:
            return None
        
        def delete_deepest_node(deepest_node: Node) -> Node:
            queue = deque([self.root])
            while queue:
                current = queue.popleft()

                if current.left == deepest_node:
                    current.left = None
                    return self.root
                if current.right == deepest_node:
                    current.right = None
                    return self.root

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

            return self.root

        queue = deque([self.root])
        while queue:
            current = queue.popleft()

            if current.val == val:
                deepest_node = self.deepest_node()
                current.val = deepest_node.val
                return delete_deepest_node(deepest_node)

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return None

    def height(self) -> int:
        if self.root is None:
            return 0

        def height_helper(node: Node) -> int:
            if node is None:
                return 0

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
            balanced = (
                balanced_left
                and balanced_right
                and abs(height_left - height_right) <= 1
            )

            return max(height_left, height_right) + 1, balanced

        return is_balanced_helper(self.root)[1]

    def node_count(self) -> int:
        def node_count_helper(node: Node) -> int:
            if node is None:
                return 0
            return node_count_helper(node.left) + node_count_helper(node.right) + 1

        return node_count_helper(self.root)

if __name__ == "__main__":
    BT = BinaryTree()

    # Insert initial elements
    vals = [5, 2, 3, 4, 10, 1, 2]
    for _ in vals:
        BT.insert(_)

    print(BT.is_balanced())
    print(BT.height())
    print(BT.inorder_traversal())
    BT.delete(5)
    print(BT.inorder_traversal())
    print(BT.node_count())