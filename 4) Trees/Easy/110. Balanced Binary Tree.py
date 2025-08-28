'''
Given a binary tree, determine if it is height-balanced.
'''

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.balanced = True

        def dfs(root):
            if not root: 
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            if left - right > 1 or right - left > 1:
                self.balanced = False
            return 1 + max(left, right)

        dfs(root)
        return self.balanced