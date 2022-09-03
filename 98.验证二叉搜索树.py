#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 经典错误 - 只判断父节点和左右子节点的值
        # [5,4,6,null,null,3,7]
        # def dfs(node):
        #     if node is None:
        #         return True
        #     tag = True
        #     if node.left:
        #         if node.left.val >= node.val:
        #             return False
        #         tag &= dfs(node.left)
        #     if node.right:
        #         if node.right.val <= node.val:
        #             return False
        #         tag &= dfs(node.right)
        #     return tag

        # 实质上，要求 root.val 应该是 left.val(lower) 和 right.val(upper) 之间的数值
        def dfs(node, upper, lower):
            if node is None:
                return True
            val = node.val
            if val <= lower or val >= upper:
                return False
            if not dfs(node.left, val, lower):
                return False
            if not dfs(node.right, upper, val):
                return False
            return True
        return dfs(root, float('inf'), float('-inf'))

# @lc code=end
