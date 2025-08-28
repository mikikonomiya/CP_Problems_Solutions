'''
You are given the root of a binary tree root. Invert the binary tree and return its root.
'''

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        root.left, root.right = root.right, root.left
        
        root.right = self.invertTree(root.right)
        root.left = self.invertTree(root.left)
        
        return root