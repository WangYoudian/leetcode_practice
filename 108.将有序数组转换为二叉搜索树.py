#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # 注：Python 中数组长度为 0 ，逻辑上为 False 
        if not nums:
            return None
        n = len(nums)
        if n == 1:
            return TreeNode(val=nums[0])
        mid = TreeNode(val=nums[n//2])
        mid.left = self.sortedArrayToBST(nums[:n//2])
        mid.right = self.sortedArrayToBST(nums[n//2 + 1:])

        return mid
# @lc code=end

