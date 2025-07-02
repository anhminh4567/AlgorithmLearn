from tree.BinaryTree import BinaryTree
parsed_math_equation = [
    '(', '3', '+', '(', '4', '*', '5', ')', ')']  # (3 + (4 * 5 ) )

# Using the information from above we can define four rules as follows:
# If the current token is a '(', add a new node as the left child of the current node, and descend to the left child.

# If the current token is in the list ['+','-','/','*'], set the root value of the current node to the operator represented by the current token. Add a new node as the right child of the current node and descend to the right child.

# If the current token is a number, set the root value of the current node to the number and return to the parent.

# If the current token is a ')', go to the parent of the current node.
root = BinaryTree(None)
pointer = root

for item in parsed_math_equation:
    if item == '(':
        tree = BinaryTree(None)
        pointer.insert_left(tree)
        pointer = tree
    elif item == ')':
        pointer = pointer.parent
    elif item in ['+', '-', '*', '/']:
        pointer.value = item
        new_node = BinaryTree(None)
        pointer.insert_right(new_node)
        pointer = new_node
    else:
        pointer.value = item
        pointer = pointer.parent

root.print_tree()
