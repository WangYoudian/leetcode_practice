#
# @lc app=leetcode.cn id=1491 lang=python3
#
# [1491] 去掉最低工资和最高工资后的工资平均值
#

# @lc code=start
class Solution:
    def average(self, salary: List[int]) -> float:
        n = len(salary)
        high, low = salary[0], salary[0]
        for i in range(n):
            high = max(high, salary[i])
            low = min(low, salary[i])
        return (sum(salary) - high - low) / (n -2)
# @lc code=end

