# Source: https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# A binary tree is symmetric if you can draw a vertical line through
# the root and the left subtree is the mirror image of right subtree

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
          
         def isMirror(t1, t2):
             if t1 == None and t2 == None:
                 return True
             if t1 == None or t2 == None:
                 return False
             return (t1.val == t2.val) and isMirror(t1.right, t2.left) and isMirror(t1.left, t2.right)
        
         return isMirror(root, root)
        