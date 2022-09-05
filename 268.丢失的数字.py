#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 丢失的数字
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nd = set(nums)
        for i in range(len(nums) + 2):
            if i not in nd:
                return i

# @lc code=end
