#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
# dfs算法过程：矩阵进行遍历，所检查的位置若为1，则岛屿数量+1
#           且将相连的1全部改成0

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(grid), len(grid[0])
        def dfs(x, y):
            grid[x][y] = "0"
            for d in DIR:
                new_x, new_y = x + d[0], y + d[1]
                if 0 <= new_x < m and 0<= new_y < n and \
                    grid[new_x][new_y] == "1":
                    dfs(new_x, new_y)
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    ans += 1
                    dfs(i, j)
        return ans



# @lc code=end

