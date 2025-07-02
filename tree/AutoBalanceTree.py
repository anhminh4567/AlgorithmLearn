# https://www.geeksforgeeks.org/self-balancing-binary-search-trees/
#https://www.w3schools.com/dsa/dsa_data_avltrees.php 
#e must keep our tree balanced. 
#AVL Tree
# An AVL tree defined as a self-balancing Binary Search Tree (BST) where the difference between heights 
# of left and right subtrees for any node cannot be more than one.
from typing import List



class BalanceTree():
    value: int = None
    left: "BalanceTree" = None
    right: "BalanceTree" = None
    parent: "BalanceTree" = None
    height: int = 0
    #       more than 0: The node is "right heavy".
    #       less than 0: The node is "left heavy".

    @property
    def is_root(self):
        return self.parent is None

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = 1
    def get_height(self):
        if not self:
            return 0
        return self.height
    def get_balance_factor(self):
        if not self or (self.left is None and self.right is None):
            return 0
        if self.left is None:
            return -1 *self.right.get_height()
        if self.right is None:
            return self.left.get_height()
        return self.left.get_height() - self.right.get_height()
    
    def search(self, value: int):
        currentNode = self
        if currentNode is None:
            return None
        while currentNode is not None:
            if currentNode.value == value:
                return currentNode
            elif value > currentNode.value:
                currentNode = currentNode.right
            elif value < currentNode.value:
                currentNode = currentNode.left
        return None
    
    def delete(self, value: int):
        pass
    def insert(self, new_val: int):
        if new_val < self.value:
            if self.left is None:
                self.left = BalanceTree(new_val)
                self.left.parent = self
            else:
                self.left = self.left.insert(new_val)
        elif new_val > self.value:
            if self.right is None:
                self.right = BalanceTree(new_val)
                self.right.parent = self
            else:
                self.right = self.right.insert(new_val)
        else:
            # Duplicate values are not allowed in this AVL tree
            return self
        # Update the balance factor and balance the tree
        self.height = 1 + max(
            self.left.get_height() if self.left else 0,
            self.right.get_height() if self.right else 0
        )

        # Get the balance factor
        balance_factor = self.get_balance_factor()

        # Balancing the tree
        # Left Left Case
        if balance_factor > 1 and new_val < self.left.value:
            return self.rotate_right()

        # Left Right Case
        if balance_factor > 1 and new_val > self.left.value:
            self.left = self.left.rotate_left()
            return self.rotate_right()

        # Right Right Case
        if balance_factor < -1 and new_val > self.right.value:
            return self.rotate_left()

        # Right Left Case
        if balance_factor < -1 and new_val < self.right.value:
            self.right = self.right.rotate_right()
            return self.rotate_left()

        return self

    
    def rotate_left(self):
        if not self.right:
            return self  # Cannot perform a left rotation if there is no right child

        right = self.right
        left_of_right_node = right.left

        # Perform the rotation
        right.left = self
        self.right = left_of_right_node

        # Update parent references
        if left_of_right_node:
            left_of_right_node.parent = self
        right.parent = self.parent
        if self.parent:
            if self.parent.left == self:
                self.parent.left = right
            else:
                self.parent.right = right
        self.parent = right

        # Update heights
        self.height = max(
            self.left.get_height() if self.left else 0,
            self.right.get_height() if self.right else 0
        ) + 1
        right.height = max(
            right.left.get_height() if right.left else 0,
            right.right.get_height() if right.right else 0
        ) + 1

        return right 
    
    def rotate_right(self):
        #  print('Rotate right on node',y.data)
        if not self.left:
            return self  # Cannot perform a right rotation if there is no left child

        left = self.left
        right_of_left_node = left.right

        # Perform the rotation
        left.right = self
        self.left = right_of_left_node

        # Update parent references
        if right_of_left_node:
            right_of_left_node.parent = self
        left.parent = self.parent
        if self.parent:
            if self.parent.left == self:
                self.parent.left = left
            else:
                self.parent.right = left
        self.parent = left

        # Update heights
        self.height = max(
            self.left.get_height() if self.left else 0,
            self.right.get_height() if self.right else 0
        ) + 1
        left.height = max(
            left.left.get_height() if left.left else 0,
            left.right.get_height() if left.right else 0
        ) + 1

        return left
        
    @classmethod
    def pre_order(self, tree: "BalanceTree", result_queue: List = []):
        result_queue.append(tree.value)
        if tree.left is not None:
            self.pre_order(tree.left, result_queue)
        if tree.right is not None:
            self.pre_order(tree.right, result_queue)

    @classmethod
    def in_order(self, tree: "BalanceTree", result_queue: List = []):
        if tree.left is not None:
            self.in_order(tree.left, result_queue)

        result_queue.append(tree.value)

        if tree.right is not None:
            self.in_order(tree.right, result_queue)
        pass

    @classmethod
    def post_order(self, tree: "BalanceTree", result_queue: List = []):
        if tree.left is not None:
            self.post_order(tree.left, result_queue)
        if tree.right is not None:
            self.post_order(tree.right, result_queue)
        result_queue.append(tree.value)

    def print_tree(self, level=0):
        print("  " * level + f"{self.value}")
        if self.left:
            self.left.print_tree(level + 1)
        if self.right:
            self.right.print_tree(level + 1)


if __name__ == "__main__":
    root = BalanceTree(10)
    # Insert values
    root.insert(20)
    root.insert(5)
    root.insert(4)
    root.insert(15)

    # Print the tree
    print("AVL Tree after insertions:")
    root.print_tree()