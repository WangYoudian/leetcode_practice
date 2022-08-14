#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
# 分析：BFS

# @lc code=start
import string
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        if root is None:
            return ans
        q = deque([[root]])

        def translate(tns):
            if len(tns) == 1:
                return str(tns[0].val)
            res = str(tns[0].val)
            for i in range(1, len(tns)):
                res += '->' + str(tns[i].val)
            return res

        while q:
            nodes = q.popleft()
            if nodes[-1].left is None and nodes[-1].right is None:
                ans.append(translate(nodes))
            # star: ※※  注意 nodes 不能被改变，防止左右子树都不为 None 时，
            # 导致 right 和 left 同时出现在同一条路径下
            if nodes[-1].left is not None:
                q.append(nodes + [nodes[-1].left])
            if nodes[-1].right is not None:
                q.append(nodes + [nodes[-1].right])

        return ans

# @lc code=end
