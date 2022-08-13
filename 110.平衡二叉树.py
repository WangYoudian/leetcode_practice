#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
# 分析：检查二叉树的高度，树本身高度是左右子树最大高度 + 1
#   当左右子树高度差大于1时，返回-1（表示不平衡），且从下层往上层走，
#   若当前节点有任意左右子树失去平衡，则整棵树就不是AVL树

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # star：※※  check不仅标识树是否平衡，还能返回平衡子树的高度
        def check(root):
            if root is None:
                return 0
            left = check(root.left)
            right = check(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            # 返回（子）树的高度
            return 1 + max(left, right)
        # 当且仅当返回值为树的高度时，才为True。
        # 若返回-1，则证明某处子结构已经失去了平衡
        return check(root) != -1

# @lc code=end

