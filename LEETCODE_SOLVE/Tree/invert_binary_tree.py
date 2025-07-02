#https://neetcode.io/problems/invert-a-binary-tree
# EASY level
from typing import Optional


root1 = [1,2,3,4,5,6,7] #[1,3,2,7,6,5,4]
root2 = [3,2,1] # [3,1,2]
root3 = [] # []
root4=[1,2]
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def print_tree(self, level=0):
        print("  " * level + f"{self.val}")
        if self.left:
            self.left.print_tree(level + 1)
        if self.right:
            self.right.print_tree(level + 1)

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        if root.left is None and root.right is None:
            return root
        
        if root.left is None:
            root.left = root.right
            root.right = None
            self.invertTree(root.left)
            return root
        if root.right is None:
            root.right = root.left
            root.left = None
            self.invertTree(root.right)
            return root
        holder = root.left
        root.left = root.right
        root.right = holder
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
    
    
solution = Solution()
tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.left.left = TreeNode(4)
tree1.left.right = TreeNode(5)
tree1.right = TreeNode(3)    
tree1.right.left = TreeNode(6)
tree1.right.right = TreeNode(7)
# tree1.print_tree()

tree1= solution.invertTree(tree1)
tree1.print_tree()


tree2 = TreeNode(3)
tree2.left = TreeNode(2)
tree2.right = TreeNode(1)
# tree2.print_tree()
tree2= solution.invertTree(tree2)
# tree2.print_tree()

tree4 = TreeNode(1)
tree4.left = TreeNode(2)
tree4.print_tree()
tree4= solution.invertTree(tree4)
tree4.print_tree()