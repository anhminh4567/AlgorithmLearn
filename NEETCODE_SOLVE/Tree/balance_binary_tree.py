# https://neetcode.io/problems/balanced-binary-tree
# # # EASY level
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True
        try:
            self.post_order_depth_cal(root)
        except ValueError:
            return False
        return True
     
    
    def post_order_depth_cal(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        left_depth = self.post_order_depth_cal(root.left)
        right_depth = self.post_order_depth_cal(root.right)
        if abs(left_depth - right_depth) > 1:
            raise ValueError("The tree is not balanced")
        return max(left_depth, right_depth) + 1
            
        
solution = Solution()
tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)
tree1.right.left = TreeNode(4)
print(solution.isBalanced(tree1)) # False
        
tree2 = TreeNode(1)
tree2.left = TreeNode(2)
tree2.right = TreeNode(3)
tree2.right.left = TreeNode(4)
tree2.right.left.left = TreeNode(5)
print(solution.isBalanced(tree2)) # False

tree3 = TreeNode(1)
tree3.left = TreeNode(2)
tree3.left.right = TreeNode(3)
tree3.right = TreeNode(2)
tree3.right.right = TreeNode(3)
tree3.right.right.right = TreeNode(4)
tree3.right.right.right.right = TreeNode(4)
print(solution.isBalanced(tree3)) # False