#
# @lc app=leetcode.cn id=1020 lang=python3
#
# [1020] 飞地的数量
#

# @lc code=start
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(grid), len(grid[0])

        def dfs(x, y):
            tag = 0
            cnt = 1
            grid[x][y] = 0
            for dx, dy in DIR:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if grid[nx][ny] == 1:
                        new_tag, new_cnt = dfs(nx, ny)
                        tag |= new_tag
                        cnt += new_cnt
                    # 防止nx和ny越界访问grid（grid[-1][-1]这种在Python也是合法的）
                    # grid[nx][ny] == 0
                    else:
                        continue
                else:
                    tag = 1
            return tag, cnt

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    t, c = dfs(i, j)
                    if t == 0:
                        ans += c
        return ans

# @lc code=end

