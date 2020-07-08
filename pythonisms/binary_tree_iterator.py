class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, collection=None):
        self.root = None
        if collection:
            for item in collection:
                self.add(item)

    def __iter__(self):
        
        def value_generator(root):
            if not root:
                return

            # <<< root >>>
            yield root.value

            # <<< left
            value_generator(root.left)

            # right >>>
            value_generator(root.right)

        return value_generator(self.root)

    def __str__(self):
        pass

    def __len__(self):
        pass

    def __eq__(self):
        pass

    def __getitem__(self, index):
        pass

    def pre_order(self):
        """This is a Depth First traversal method. It prioritizes printing the `root` first, then looks to print `left` if left is not `None`, and lastly looks `right`."""
        collection = []

        def walk(root):
            if not root:
                return

            # <<< root >>>
            collection.append(root.value)

            # <<< left
            walk(root.left)

            # right >>>
            walk(root.right)

        # end
        walk(self.root)

        return collection

class BinarySearchTree(BinaryTree):
    def add(self, value):
        """This will add a new element to the tree, based on a tradtional binary search tree condtional. If value is smaller than the root it will be added to the left, else add to the right."""

        node = Node(value)

        # Handles empty tree
        if not self.root:
            self.root = node
            return

        def walk(root, new_node):

            if not root:
                return

            # <<< left
            if new_node.value < root.value:

                if not root.left:
                    root.left = new_node
                else:
                    walk(root.left, new_node)

            # right >>>
            else:
                if not root.right:
                    root.right = new_node
                else:
                    walk(root.right, new_node)

        walk(self.root, node)