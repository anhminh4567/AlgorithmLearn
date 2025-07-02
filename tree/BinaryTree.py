
from typing import List


class BinaryTree():
    value: str = None
    left: "BinaryTree" = None
    right: "BinaryTree" = None
    parent: "BinaryTree" = None

    @property
    def is_root(self):
        return self.parent is None

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def insert_left(self, new_node: "BinaryTree"):
        if self.left is None:
            self.left = new_node
            new_node.parent = self
        else:
            current_left = self.left
            self.left = new_node
            new_node.parent = self
            leaf_node = new_node
            while leaf_node.left is not None:
                leaf_node = leaf_node.left
            leaf_node.left = current_left
        return self

    def insert_right(self, new_node: 'BinaryTree'):
        if self.right is None:
            self.right = new_node
            new_node.parent = self
        else:
            current_right = self.right
            self.right = new_node
            new_node.parent = self
            leaf_node = new_node
            while leaf_node.right is not None:
                leaf_node = leaf_node.right
            leaf_node.right = current_right
        return self

    @classmethod
    def pre_order(self, tree: "BinaryTree", result_queue: List = []):
        '''In a preorder traversal, we visit the root node first,
        then recursively do a preorder traversal of the left subtree, 
        followed by a recursive preorder traversal of the right subtree.'''
        result_queue.append(tree.value)
        if tree.left is not None:
            self.pre_order(tree.left, result_queue)
        if tree.right is not None:
            self.pre_order(tree.right, result_queue)

    @classmethod
    def in_order(self, tree: "BinaryTree", result_queue: List = []):
        '''In an inorder traversal, we recursively do an inorder 
        traversal on the left subtree, visit the root node, and finally 
        do a recursive inorder traversal of the right subtree.'''
        if tree.left is not None:
            self.in_order(tree.left, result_queue)

        result_queue.append(tree.value)

        if tree.right is not None:
            self.in_order(tree.right, result_queue)
        pass

    @classmethod
    def post_order(self, tree: "BinaryTree", result_queue: List = []):
        '''In a postorder traversal, we recursively do a postorder 
        traversal of the left subtree and the right subtree followed by 
        a visit to the root node.'''
        if tree.left is not None:
            self.post_order(tree.left, result_queue)
        if tree.right is not None:
            self.post_order(tree.right, result_queue)
        result_queue.append(tree.value)

    def print_tree(self, level=0):
        # Print the current node with indentation based on its level
        print("  " * level + f"{self.value}")
        # Recursively print the left and right branches
        if self.left:
            self.left.print_tree(level + 1)
        if self.right:
            self.right.print_tree(level + 1)
