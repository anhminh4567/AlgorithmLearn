# https://neetcode.io/problems/depth-of-binary-tree
# EASY level
from calendar import c
from typing import Optional

root1 = [1,2,3,None,None,4] # depth = 3
root2 = [] # depth = 0
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        current_max_height = 0
        if root is None :
            return 0
        current_max_height += 1
        if root.left is None and root.right is None:
            return current_max_height
        
        def in_order_traversal(node: Optional[TreeNode], current_depth: int):
            nonlocal current_max_height
            if node is None:
                return
            current_depth += 1
            if node.left is None and node.right is None:
                current_max_height = max(current_max_height, current_depth)
                return
            if node.left:
                in_order_traversal(node.left,  current_depth)
            if node.right:
                in_order_traversal(node.right, current_depth)
        
        current_dept = current_max_height
        if root.left:
            in_order_traversal(root.left, current_dept)
        if root.right:
            in_order_traversal(root.right, current_dept)
        return current_max_height
    
solution = Solution()
tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)
tree1.right.left = TreeNode(4)
print(solution.maxDepth(tree1))
        
        
    
tree2 = None
print(solution.maxDepth(tree2)) # 0   