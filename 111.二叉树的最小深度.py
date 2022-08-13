#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        # 节点左右子树只有一边
        if left == 0 or right == 0:
            return max(left, right) + 1
        # 递归的目标，找最短路径
        else:
            return min(left, right) + 1

# @lc code=end

