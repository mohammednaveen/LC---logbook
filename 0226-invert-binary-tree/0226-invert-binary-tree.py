# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        # Approach number 1 
        if root is None:
            return 
        
        self.invertTree(root.left)
        self.invertTree(root.right)

        root.left, root.right = root.right,root.left

        return root



        # # Approach number 2
        # if root is None:
        #     return None

        # left = self.invertTree(root.right)
        # right = self.invertTree(root.left)

        # root.left = left
        # root.right = right
        # return root



        # # Approach number 3
        # if not root:
        #     return None

        # queue = [root]
        # while queue:
        #     current = queue.pop(0)
        #     current.left, cuurent.right = current.right, current.left
        #     if current.left:
        #         queue.append(current.left)
        #     if current.right:
        #         queue.append(current.right)
        # return root
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        