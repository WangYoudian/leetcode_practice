#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#
from copy import deepcopy

# @lc code=start
class Solution:
    # def minimumTotal(self, triangle: List[List[int]]) -> int:
    #     n = len(triangle)
    #     dp = [[0] * n for i in range(n)]
    #     dp[0][0] = triangle[0][0]
    #     for i in range(1, n):
    #         dp[i][0] = dp[i-1][0] + triangle[i][0]
    #     for j in range(1, n):
    #         for k in range(1, j+1):
    #             if k == j:
    #                 dp[j][k] = triangle[j][k] + dp[j-1][k-1]
    #             else:
    #                 dp[j][k] = min(dp[j-1][k-1], dp[j-1][k]) + triangle[j][k]
        
    #     return min(dp[n-1])

    # optimization 1: O(n) storage
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [0 for _ in range(n)]
        dp[0] = triangle[0][0]
        
        for i in range(1, n):
            # 等腰直角三角形斜边的格子在一维数组的落位
            dp[i] = dp[i-1] + triangle[i][i]
            # 避免从左往右遍历时，前一个值被覆盖，故而从右往左
            for j in range(i-1, 0, -1):
                dp[j] = min(dp[j-1], dp[j]) + triangle[i][j]
            dp[0] += triangle[i][0]
        
        return min(dp)



# @lc code=end

