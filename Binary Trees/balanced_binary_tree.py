# Source: https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# A binary tree is said to be balanced if for each node in the tree, 
# the difference in the height of its left and right subtrees is
# at most one.
# Time Complexity: O(n log(n))
# Space Complexity: O(n)

class Solution:
    def height(self, node):
        if not node:
            return -1
        
        return max(self.height(node.left), self.height(node.right)) + 1
    
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        leftH = self.height(root.left)
        rightH = self.height(root.right)
        if abs(leftH - rightH) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        else:
            return False