#
# @lc app=leetcode.cn id=1822 lang=python3
#
# [1822] 数组元素积的符号
#

from functools import reduce

# @lc code=start
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        t = reduce(lambda x, y : x * y, nums)
        if t > 0:
            return 1
        elif t < 0:
            return -1
        else:
            return 0
# @lc code=end

