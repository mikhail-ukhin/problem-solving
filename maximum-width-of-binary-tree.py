# Given a binary tree, write a function to get the maximum width of the given tree. 
# The width of a tree is the maximum width among all levels. 
# The binary tree has the same structure as a full binary tree, but some nodes are null.

# The width of one level is defined as the length between the end-nodes (the leftmost and right most 
# non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

# Note: Answer will in the range of 32-bit signed integer.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        if not root: return 0
        if not root.left and not root.right: return 1

        current_level = [root]
        max_width = 0

        while len(current_level):
            lp, rp = None, None
            next_level = []

            for index, e in enumerate(current_level):
                if not lp and e:
                    lp = index
                elif e:
                    rp = index

                if e:
                    next_level.append(e.left)
                    next_level.append(e.right)
                else:   
                    next_level.append(None)
                    next_level.append(None)      

            if lp and rp:
                max_width = rp - lp

            if all(not x for x in next_level):
                break
            else:
                current_level = next_level

        return max_width