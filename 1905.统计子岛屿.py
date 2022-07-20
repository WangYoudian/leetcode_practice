#
# @lc app=leetcode.cn id=1905 lang=python3
#
# [1905] 统计子岛屿
# dfs过程分析：遍历grid2，遇到grid2[i][j]为1时，检查grid1对应
#       位置是否也为1即可

# @lc code=start
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(grid2), len(grid2[0])

        def dfs(x, y):
            # 必须是在这里给tag赋值而非在nx和ny越界判断那里加条件
            # 避免一些在矩阵中央孤立的1被计入
            if grid1[x][y] == 1:
                tag = 1
            else:
                tag = 0
            
            grid2[x][y] = 0
            for dx, dy in DIR:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid2[nx][ny] == 1:
                    tag &= dfs(nx, ny)
                # grid2[nx][ny] == 0 或者 越界
                else:
                    continue
            return tag

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    ans += dfs(i, j)
        return ans

# @lc code=end

