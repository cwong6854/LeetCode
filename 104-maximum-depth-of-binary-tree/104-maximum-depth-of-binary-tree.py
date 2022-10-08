# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Counter for Maximum Depth
        maxDepth = 1
        depth = 1
        # if there's a left or right, we will assign variable, and creat helper functions to traverse the left, right or both
        def Traverse(node, depth):
            # when we traverse, depth increases
            depth += 1
            hasLeft = False
            hasRight = False
            if node.left:
                hasLeft = True
            if node.right:
                hasRight = True
            if hasLeft and hasRight:
                l_depth = Traverse(node.left, depth)
                r_depth = Traverse(node.right, depth)
                depth = max(depth, l_depth, r_depth)
            else:
                if hasLeft:
                    l_depth = Traverse(node.left, depth)
                    depth = max(depth, l_depth)
                elif hasRight:
                    r_depth = Traverse(node.right, depth)
                    depth = max(depth, r_depth)
                else:
                    print()
            return depth
        if root == None:
            return 0
        if root.left:
            maxDepth = max(maxDepth, Traverse(root.left, depth))
        if root.right:
            maxDepth = max(maxDepth, Traverse(root.right, depth))
        return maxDepth