class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insertion
    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert(data, node.left)
        else:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert(data, node.right)

    # Search
    def search(self, data):
        if self.root:
            return self._search(data, self.root)
        return None

    def _search(self, data, node):
        node.data = int(node.data)
        if data == node.data:
            return node
        elif data < node.data and node.left:
            return self._search(data, node.left)
        elif data > node.data and node.right:
            return self._search(data, node.right)

    # Deletion
    def delete(self, data):
        self.root = self._delete(self.root, data)

    def _delete(self, node, data):
        if not node:
            return node
        if data < node.data:
            node.left = self._delete(node.left, data)
        elif data > node.data:
            node.right = self._delete(node.right, data)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp_val = self._min_value_node(node.right)
            node.data = temp_val.data
            node.right = self._delete(node.right, temp_val.data)
        return node

    def _min_value_node(self, node):
        current = node
        while(current.left is not None):
            current = current.left
        return current

    # In-Order Traversal (Bypass in direct order)
    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root
        res = []
        if node.left:
            res = self.inorder_traversal(node.left)
        res.append(node.data)
        if node.right:
            res = res + self.inorder_traversal(node.right)
        return res

    # Pre-Order Traversal (Bypass in centered/symmetrical order)
    def preorder_traversal(self, node=None):
        if node is None:
            node = self.root
        res = []
        res.append(node.data)
        if node.left:
            res = res + self.preorder_traversal(node.left)
        if node.right:
            res = res + self.preorder_traversal(node.right)
        return res

    # Post-Order Traversal (Bypass in reverse order)
    def postorder_traversal(self, node=None):
        if node is None:
            node = self.root
        res = []
        if node.left:
            res = self.postorder_traversal(node.left)
        if node.right:
            res = res + self.postorder_traversal(node.right)
        res.append(node.data)
        return res
