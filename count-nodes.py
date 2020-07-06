# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        nodes = [root]
        count = 0
        
        while nodes:
            node = nodes.pop()
            count += 1

            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)

        return count            
        