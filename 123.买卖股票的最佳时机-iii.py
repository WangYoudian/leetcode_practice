#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#

# 注意这一【常识】：股票交易允许同一天买卖
# 思路：buy1, sell1, buy2, sell2
# 最终分析，买卖2次收益最高
# 状态转移方程一步步可优化

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
# @lc code=end

