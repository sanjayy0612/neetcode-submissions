# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def checksam(self, a, b):
        if not a and not b:
            return True 
        if not a or not b:
            return False
        
        if a.val != b.val:
            return False
        
        return self.checksam(a.left,b.left) and self.checksam(a.right,b.right)
    def dfs(self, root, subtree):
        if not root:
            return False
        if root.val==subtree.val and self.checksam(root,subtree):
            return True 
        return self.dfs(root.left, subtree) or self.dfs(root.right, subtree)
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.dfs(root,subRoot)