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
        
        result = []
        queue = [root]
        
        if root == None: return []
        
        while queue:
            nodes = []
            count = len(queue)
            for _ in range(count):
                x = queue.pop(0)
                nodes.append(x.val)
                if x.left != None:
                    queue.append(x.left)
                if x.right != None:
                    queue.append(x.right)
            result.append(nodes)
            
        return result
                
            
            