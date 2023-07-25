# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):        
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, h):
            if not root:
                return h
            return max(dfs(root.left, h+1), dfs(root.right, h+1))
        
        return dfs(root, 0)
    