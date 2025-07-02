
import sys


class Node():
    value: str = None
    left: 'Node' = None
    right: 'Node' = None

    def __init__(self, value):
        self.value = value

    def addLeft(self, new_node: 'Node'):
        self.left = new_node
        return self

    def addRight(self, new_node: 'Node'):
        self.right = new_node
        return self


def buildTree(root_value: str):
    return Node(root_value)


def insertLeft(parentNode: Node, new_node: Node):
    if parentNode.left is None:
        parentNode.left = new_node
    else:
        current_left = parentNode.left
        parentNode.left = new_node
        # get the leaf node of the new node on the left
        leaf_node = new_node
        while leaf_node.left is not None:
            leaf_node = leaf_node.left
        leaf_node.left = current_left
    return parentNode


def insertRight(parentNode: Node, new_node: Node):
    if parentNode.right is None:
        parentNode.right = new_node
    else:
        current_right = parentNode.right
        parentNode.right = new_node
        # get the leaf node of the new node on the left
        leaf_node = new_node
        while leaf_node.right is not None:
            leaf_node = leaf_node.right
        leaf_node.right = current_right
    return parentNode


def print_branch(current_branch: Node, level=0):
    if current_branch is None:
        return

    # Print the current node with indentation based on its level
    print("  " * level + f"{current_branch.value}")

    # Recursively print the left and right branches
    if current_branch.left:
        print_branch(current_branch.left, level + 1)
    if current_branch.right:
        print_branch(current_branch.right, level + 1)


ttree = buildTree('a')

bBranch = buildTree('b')
insertRight(bBranch, Node('d'))

cBranch = buildTree('c')
insertLeft(cBranch, Node('e'))
insertRight(cBranch, Node('f'))

insertLeft(ttree, bBranch)
insertRight(ttree, cBranch)

print_branch(ttree)


print(sys.path)
