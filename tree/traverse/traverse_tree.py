# Book
# ├── Chapter1
# │   ├── Section 1.1
# │   └── Section 1.2
# │       ├── Section 1.2.1
# │       └── Section 1.2.2
# └── Chapter2
#     ├── Section 2.1
#     └── Section 2.2
#         ├── Section 2.2.1
#         └── Section 2.2.2

from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
print(sys.path)


from tree.BinaryTree import BinaryTree


root = BinaryTree('Book')
root.insert_left(BinaryTree('Chapter1'))
root.insert_right(BinaryTree('Chapter2'))

root.left.insert_left(BinaryTree('Section 1.1'))
root.left.insert_right(BinaryTree('Section 1.2'))
root.left.right.insert_left(BinaryTree('Section 1.2.1'))
root.left.right.insert_right(BinaryTree('Section 1.2.2'))
root.right.insert_left(BinaryTree('Section 2.1'))
root.right.insert_right(BinaryTree('Section 2.2'))
root.right.right.insert_left(BinaryTree('Section 2.2.1'))
root.right.right.insert_right(BinaryTree('Section 2.2.2'))

root.print_tree()
result_queue = []
# pre_order = []
print("-------------------------------Pre-order Traversal:")
BinaryTree.pre_order(root, result_queue=result_queue)
print(result_queue)
# in_order = []
print("-------------------------------In-order Traversal:")
BinaryTree.in_order(root, result_queue=result_queue)
print(result_queue)
# post_order = []
print("-------------------------------Post-order Traversal:")
BinaryTree.post_order(root, result_queue=result_queue)
print(result_queue)
