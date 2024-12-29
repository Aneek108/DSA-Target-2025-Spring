def node_count(self) -> int:
        def node_count_helper(node: Node) -> int:
            if node is None:
                return 0
            return node_count_helper(node.left) + node_count_helper(node.right) + node.count

        return node_count_helper(self.root)