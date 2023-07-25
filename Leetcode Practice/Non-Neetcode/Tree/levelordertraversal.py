# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # initialize q, go through checks of size and pop, and at the end add
        # its left and right children for next height iteration
        r = []
        q = []
        if root:
            q.append(root)

        while q:
            s = len(q)
            l = []

            for i in range(s):
                node = q.pop(0)
                l.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            r.append(l)

        return r
