#
# @lc app=leetcode.cn id=919 lang=python3
#
# [919] 完全二叉树插入器
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root

    def insert(self, val: int) -> int:
        """
        层次优先遍历
        :param val:
        :return:
        """
        q = deque([self.root])
        while q:
            cur = q.popleft()
            if cur.left is None:
                cur.left = TreeNode(val)
                return cur.val
            elif cur.right is None:
                cur.right = TreeNode(val)
                return cur.val
            # 左右孩子都不为 None
            else:
                q.append(cur.left)
                q.append(cur.right)

    def get_root(self) -> TreeNode:
        return self.root


# @lc code=end

