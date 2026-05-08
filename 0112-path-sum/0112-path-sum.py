# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        # def dfs(root, target):
        #     if root.left is None and root.right is None:
        #         return (target-root.val) == 0
        #     left = dfs(root.left, target-root.left.val)
        #     right = dfs(root.right, target-root.right.val)
        #     return left or right

        # if root is None:
        #     return False
        
        # targetSum -= root.val

        # if root.left is None and root.right is None:
        #      return targetSum == 0
        
        # return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
        

        if root is None:
            return False

        if not root.left and not root.right and targetSum-root.val == 0:
            return True

        return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)