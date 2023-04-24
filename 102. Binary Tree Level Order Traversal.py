# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        
        queue = collections.deque()
        queue.append(root)
        
        while queue:
            queueSize = len(queue)
            output2 = []
            for i in range(queueSize):
                node = queue.popleft()
                if node:
                    output2.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if len(output2) > 0:    output.append(output2)
        return output