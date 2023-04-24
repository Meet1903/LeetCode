"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        output = []
        
        def pOrder(node):
            if node is None: return
            for child in node.children:
                pOrder(child)
            output.append(node.val)
        
        pOrder(root)
        return output