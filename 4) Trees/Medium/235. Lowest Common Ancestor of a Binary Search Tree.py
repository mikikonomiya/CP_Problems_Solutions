'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as 
the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
'''

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
            if not root:
                return

            if min(p.val, q.val) > root.val:
                return self.lowestCommonAncestor(root.right, p, q)
            elif max(p.val, q.val) < root.val:
                return self.lowestCommonAncestor(root.left, p, q)
            else: 
                return root