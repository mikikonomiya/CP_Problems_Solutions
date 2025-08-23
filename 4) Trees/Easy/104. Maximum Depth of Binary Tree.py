'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the 
longest path from the root node down to the farthest leaf node.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depth(root):
            if not root:
                return 0
            height = 0
            if root.right and root.left:
                height = max(depth(root.right) + 1, depth(root.left) + 1)
            elif root.right:
                height = depth(root.right) + 1
            else:
                height = depth(root.left) + 1
            return height
        return depth(root)