#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机

# 思路
# 1.记录【今天之前买入的最小值】
# 2.计算【今天之前最小值买入，今天卖出的获利】，也即【今天卖出的最大获利】
# 3.比较【每天的最大获利】，取最大值即可
# 注意：不是从头遍历找最小值，而是以“今天”为一个锚点，减去之前的最小；
#      同时确保这个最大获利最大

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        if len(prices) <= 1:
            return max_profit
        min_price = prices[0]
        for i in range(1, len(prices)):
            max_profit = max([max_profit, prices[i] - min_price])
            min_price = min([min_price, prices[i]])
        return max_profit



# @lc code=end

