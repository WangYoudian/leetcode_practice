#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
# 注意：并不是严格的递归子结构，左右子树分别为对称树，但整棵树不一定对称
# 分析：两个树在什么情况下互为镜像？
# 1.它们的两个根结点具有相同的值
# 2.每个树的右子树都与另一个树的左子树镜像对称

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(t1, t2):
            # star: ※※  判断树节点是否为 None 的 if 写法
            if t1 is None and t2 is None:
                return True
            # t1 和 t2 中有一个为 None 
            if t1 is None or t2 is None:
                return False
            return t1.val == t2.val and check(t1.left, t2.right) and\
                check(t2.left, t1.right)
        # 等效于检查 root 自身镜像，负负得正
        return check(root, root)

# @lc code=end
