# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return [0, True] # [height, balanced bool]
            l, r = dfs(node.left), dfs(node.right)
            balanced = l[1] and r[1] and abs(l[0]-r[0]) <= 1
            return ([1 + max(l[0], r[0]), balanced])

        return dfs(root)[1]

