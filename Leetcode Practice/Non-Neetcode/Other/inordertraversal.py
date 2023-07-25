# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def traverse(self, root, res):
        if root:
            # if the root exists, traverse left first, then middle, then right
            self.traverse(root.left, res)
            res.append(root.val)
            self.traverse(root.right, res)

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.traverse(root, res)
        return res
