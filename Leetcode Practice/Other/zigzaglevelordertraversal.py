# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q = []
        r = []
        switch = 0
        if root:
            q.append(root)

        switch = 0
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

            if switch % 2:
                l.reverse()

            r.append(l)

            switch += 1

        return r

