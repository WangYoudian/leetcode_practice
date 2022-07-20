#
# @lc app=leetcode.cn id=741 lang=python3
#
# [741] 摘樱桃
#
# 类题分析：网络流入门题，方格取数，最小费用最大流
# 思路：一开始想两步dp，但两步最优并非全局最优。
# 这题可以看作同时dfs两条合法路径，得着眼于如何处理重复
# 最好的思路是，将往返两条路看做是两个人从同一点出发，最终走到(N-1, N-1)位置
# 过程中可能出现位置重复，可能位置呼唤（设置x_1, x_2，不妨设x_1<=x_2）

# @lc code=start
from math import inf
from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]):
        n = len(grid)
        f = [[[-inf] * n for _ in range(n)] for _ in range(2 * n - 1)]
        # 从grid[0][0]出发，途径grid[N-1][N-1]的近似过程
        f[0][0][0] = grid[0][0]
        # k的范围从1到2n-2
        for k in range(1, 2 * n - 1):
            # x1的范围，右上角时最小，左下角时最大;且x1从0开始,即从出发点只做了横向平移
            for x1 in range(max(k - n + 1, 0), min(k + 1, n)):
                y1 = k - x1
                if grid[x1][y1] == -1:
                    continue
                for x2 in range(x1, min(k + 1, n)):
                    y2 = k - x2
                    if grid[x2][y2] == -1:
                        continue
                    # 由于实际中需要对比的四种情况中，有的因为处在矩阵边缘可能不存在，
                    # 这里比较大小之前需要判断这些前置状态是否存在
                    res = f[k - 1][x1][x2]
                    # f[k-1]矩阵有左前置格子
                    if x1:
                        res = max(res, f[k - 1][x1 - 1][x2])
                    if x1 and x2:
                        res = max(res, f[k - 1][x1 - 1][x2 - 1])
                    if x2:
                        res = max(res, f[k - 1][x1][x2 - 1])
                    res += grid[x1][y1]
                    # 避免摘同一个樱桃
                    if x1 != x2:
                        res += grid[x2][y2]
                    f[k][x1][x2] = res
        return max(f[-1][-1][-1], 0)

# @lc code=end
