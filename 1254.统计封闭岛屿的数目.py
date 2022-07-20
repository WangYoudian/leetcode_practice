#
# @lc app=leetcode.cn id=1254 lang=python3
#
# [1254] 统计封闭岛屿的数目
# dfs算法过程分析：在搜索过程中，对于“封闭”这一概念的等价是：
#       陆地0的周围只有陆地0或者海域1，并不存在边界，
#       否则，这一片岛屿就不是封闭的
#   对于不是封闭的岛屿，使用一个内部变量tag进行标记，最终dfs返回该标记

# @lc code=start
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(x, y):
            # 模拟岛屿沉没
            grid[x][y] = 1
            tag = 1
            for dx, dy in DIR:
                nx, ny = x + dx, y + dy
                if not (0<= nx < m and 0<=ny<n):
                    tag = 0
                # 岛屿遍历完成之后，整体统计的tag才返回
                elif grid[nx][ny] == 0:
                    tag &= dfs(nx, ny)
            return tag

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    ans += dfs(i, j)
        return ans
# @lc code=end

