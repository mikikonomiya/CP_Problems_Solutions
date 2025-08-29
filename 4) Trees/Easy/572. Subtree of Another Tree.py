'''
Given the roots of two binary trees root and subRoot, return true if there is a subtree of 
root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in 
tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
'''

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        if self.isSame(root, subRoot):
            return True
        else:
            return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)

    def isSame(self, root, subRoot):
        if not root and not subRoot:
            return True
        
        if root and subRoot and root.val == subRoot.val:
            return self.isSame(root.right, subRoot.right) and self.isSame(root.left, subRoot.left)
        else:
            return False