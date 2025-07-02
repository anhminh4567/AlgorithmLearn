# https://neetcode.io/problems/valid-binary-search-tree
# # MEDIUM level
from typing import Optional
# A valid binary search tree satisfies the following constraints:

# The left subtree of every node contains only nodes with keys less than the node's key.
# The right subtree of every node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees are also binary search trees.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        min = float("-inf")
        max = float("inf")
        return self.depth_first_check(root, min, max)
    
    def depth_first_check(self,node:Optional[TreeNode], min:float, max:float) -> bool:
        if node is None:
            return True
        if not (min < node.val < max):
            return False
        left_valid = self.depth_first_check(node.left, min, node.val)
        right_valid = self.depth_first_check(node.right, node.val, max)
  
        
        return left_valid and right_valid