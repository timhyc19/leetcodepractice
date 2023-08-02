"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {} # old node, new node
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node] # return the copy of the node
            # otherwise, create the node copy and insert into hashmap
            newNode = Node(node.val)
            oldToNew[node] = newNode
            for nei in node.neighbors:
                # to my new copy, append its neighbor copies by calling dfs
                newNode.neighbors.append(dfs(nei))
            return newNode
        
        return dfs(node) if node else None
    